import os
import flask
from wtforms import StringField, DateField, SubmitField, DateTimeField
from flask_wtf import FlaskForm
from flask import request, jsonify, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import desc

from flask_mail import Mail, Message
from sqlalchemy.event import listens_for
import sqlite3
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = os.environ.get("FLASK_S_SECRET", "default_secret_key")


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("sqlite:///"+"COOL_DB")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv("GMAIL")
app.config["MAIL_PASSWORD"] = os.getenv("GPASS")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("GMAIL")

mail = Mail(app)


class MealRecord(db.Model):
    __tablename__ = "inject"

    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.String(255))
    meal = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # created_at = db.Column(db.String)


class MyForm(FlaskForm):
    units = StringField("Units")
    meal = StringField("Meal")
    # date = DateField('created_at')
    submit = SubmitField("Submit")
    # date = DateTimeField('created_at', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')


@listens_for(MealRecord, "after_insert")
def after_meal_record_insert(mapper, connection, target):
    # Customize the email content and recipient
    subject = "New Meal Record Added"
    recipient = os.getenv("WP")
    body = f"A new meal record with id {target.id} has been added to the database."
    sender = os.getenv("GMAIL")
    send_email(subject, recipient, body)


def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route("/", methods=["GET"])
def home():
    # Fetch data from the database
    conn = sqlite3.connect(os.getenv("COOL_DB"))
    cur = conn.cursor()
    cur.execute("SELECT * FROM inject")
    data = cur.fetchall()
    # Get search query from the form
    search_query = request.args.get("search", "")
    date_filter = request.args.get("date", "")
    id_filter = request.args.get("id", "")

    query = "SELECT * FROM inject WHERE 1"

    if search_query:
        query += f" AND meal LIKE '%{search_query}%'"

    if date_filter:
        query += f" AND created_at LIKE '%{date_filter}%'"

    if id_filter:
        query += f" AND id LIKE '%{id_filter}%'"

    cur.execute(query)
    meal_data = cur.fetchall()

    # Close the database connection
    conn.close()

    # Render HTML template with the fetched data
    return render_template("index.html", inject=meal_data)


@app.route("/get_meal_records", methods=["GET"])
def get_meal_records():
    meal_records = MealRecord.query.all()

    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        records_list.append(
            {
                "id": record.id,
                "units": record.units,
                "meal": record.meal,
                "created_at": record.created_at,
            }
        )
    return render_template("meals.html", meals=meal_records)


@app.route("/get-meal-records-desc", methods=["GET"])
def get_meal_records_desc():
    meal_records = MealRecord.query.order_by(desc(MealRecord.created_at)).all()

    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        records_list.append(
            {
                "id": record.id,
                "units": record.units,
                "meal": record.meal,
                "created_at": record.created_at,
            }
        )
    return render_template("meals_desc.html", meals=meal_records)


@app.route("/get_meal_records_uniq/<int:record_id>", methods=["GET"])
def get_meal_records_uniq(record_id):
    meal_record = MealRecord.query.get(record_id)

    if meal_record:
        return render_template("meals_single.html", meals=meal_record)
    else:
        return jsonify({"message": "Record Not Found"}), 404


@app.route("/api/v1/resources/injects/all", methods=["GET"])
def api_all():
    conn = sqlite3.connect(os.getenv("COOL_DB"))
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM inject").fetchall()
    return jsonify(all_books)


@app.route("/add-meal", methods=["GET", "POST"])
def add_meal():
    form = MyForm()

    if form.validate_on_submit():
        # Process the form data
        units = form.units.data
        meal = form.meal.data
        # created_at = form.date.data

        # Store in the database
        new_entry = MealRecord(units=units, meal=meal)
        db.session.add(new_entry)
        try:
            db.session.commit()
        except Exception as e:
            print(f"Database commit error: {e}")

        # Clear the form fields after successful submission
        form.units.data = ""
        form.meal.data = ""
        # form.date.data = ''

        # Redirect to the same route to avoid resubmission on page refresh
        return redirect(url_for("get_meal_records_desc"))

        # Your form processing logic here

    # Print validation errors
    print(form.errors)
    return render_template("add_meal.html", form=form)


@app.route("/api/v1/resources/injects/create", methods=["POST"])
def api_create():
    units = request.form["units"]
    meals = request.form["meal"]
    subject = request.form["subjectId"]

    conn = sqlite3.connect(os.getenv("COOL_DB"))
    conn.row_factory = dict_factory
    cur = conn.cursor()
    new_inject = cur.execute(
        "INSERT INTO inject (units, meal, subjectId) VALUES (?, ?, ?)",
        (units, meals, subject),
    )

    conn.commit()
    return f"New Inject Inserted", 201


@app.route("/api/v1/resources/square/<int:num>", methods=["GET"])
def square(num):
    return jsonify({"square": num**2})


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route("/api/v1/resources/injects", methods=["GET"])
def api_filter():
    query_parameters = request.args
    id = query_parameters.get("id")
    units = query_parameters.get("units")
    subject = query_parameters.get("subjectId")

    query = "SELECT * FROM inject WHERE"
    to_filter = []

    if id:
        query += " id=? AND"
        to_filter.append(id)
    if units:
        query += " units=? AND"
        to_filter.append(units)
    if subject:
        query += " subjectId=? AND"
        to_filter.append(subject)
    if not (id or units or subject):
        return page_not_found(404)

    query = query[:-4] + ";"

    conn = sqlite3.connect(os.getenv("COOL_DB"))
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
