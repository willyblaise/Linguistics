import flask
from flask import request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jimmycooks/sqlite/cool.db'

db = SQLAlchemy(app)

class MealRecord(db.Model):
    __tablename__ = 'inject'

    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.String(255))
    meal = db.Column(db.String(255))
    created_at = db.Column(db.String)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    # Fetch data from the database
     conn = sqlite3.connect('/home/jimmycooks/sqlite/cool.db')
     cur = conn.cursor()
     cur.execute("SELECT * FROM inject")
     data = cur.fetchall()
         # Get search query from the form
     search_query = request.args.get('search', '')
     date_filter = request.args.get('date', '')

    # Fetch data from the 'people' table, filtered by search query
    # query = f"SELECT * FROM inject WHERE meal LIKE '%{search_query}%'"
    # cur.execute(query)
    # meal_data = cur.fetchall()

     query = "SELECT * FROM inject WHERE 1"

     if search_query:
         query += f" AND meal LIKE '%{search_query}%'"

     if date_filter:
         query += f" AND created_at LIKE '%{date_filter}%'"

     cur.execute(query)
     meal_data = cur.fetchall()
    # Close the database connection
     conn.close()

    # Render HTML template with the fetched data
     return render_template('index.html', inject=meal_data)
#    return '''<h1>Distant Reading Archive</h1>
#<p>A prototype API for distant reading of science fiction novels.</p>'''
     #return render_template('index.html', inject=data)

@app.route('/get_meal_records', methods=['GET'])
def get_meal_records():
    meal_records = MealRecord.query.all()
    
    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        records_list.append({
            'id': record.id,
            'units': record.units,
            'meal': record.meal,
            #'created_at': record.created_at.strftime('%Y-%m-%d')  # Convert date to string for JSON serialization
            'created_at': record.created_at  # Convert date to string for JSON serialization
        })
    #data = jsonify(records_list)
    return render_template('meals.html', meals=meal_records)

@app.route('/get_meal_records_desc', methods=['GET'])
def get_meal_records_desc():
    #meal_records = MealRecord.query.all()
    meal_records = MealRecord.query.order_by(desc(MealRecord.created_at)).all()
    
    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        records_list.append({
            'id': record.id,
            'units': record.units,
            'meal': record.meal,
            #'created_at': record.created_at.strftime('%Y-%m-%d')  # Convert date to string for JSON serialization
            'created_at': record.created_at  # Convert date to string for JSON serialization
        })
    #data = jsonify(records_list)
    return render_template('meals_desc.html', meals=meal_records)

@app.route('/get_meal_records_uniq/<int:record_id>', methods=['GET'])
def get_meal_records_uniq(record_id):
    meal_record = MealRecord.query.get(record_id)
    
    if meal_record:
        return render_template('meals_single.html', meals=meal_record)
    else:
        return jsonify({'message': 'Record Not Found'}), 404
    # Convert the query result to a list of dictionaries
   # records_list = []
   # for record in meal_records:
   #     records_list.append({
   #         'id': record.id,
   #         'units': record.units,
   #         'meal': record.meal,
   #         #'created_at': record.created_at.strftime('%Y-%m-%d')  # Convert date to string for JSON serialization
   #         'created_at': record.created_at  # Convert date to string for JSON serialization
   #     })
    #data = jsonify(records_list)
    #return render_template('meals_desc.html', meals=meal_records)

@app.route('/api/v1/resources/injects/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('/home/jimmycooks/sqlite/cool.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    #all_books = cur.execute('SELECT * FROM inject;').fetchall()
    all_books = cur.execute('SELECT * FROM inject').fetchall()

    return jsonify(all_books)

@app.route('/api/v1/resources/injects/create', methods=['POST'])
def api_create():

    units   = request.form["units"]
    meals   = request.form["meal"]
    subject = request.form["subjectId"]


    conn = sqlite3.connect('/home/jimmycooks/sqlite/cool.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    new_inject = cur.execute('INSERT INTO inject (units, meal, subjectId) VALUES (?, ?, ?)', (units, meals, subject))

    conn.commit()
    return f"New Inject Inserted", 201


@app.route('/api/v1/resources/square/<int:num>', methods = ['GET'])
def square(num):
    return jsonify({'square': num ** 2})


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/injects', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    units = query_parameters.get('units')
    subject = query_parameters.get('subjectId')

    query = "SELECT * FROM inject WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if units:
        query += ' units=? AND'
        to_filter.append(units)
    if subject:
        query += ' subjectId=? AND'
        to_filter.append(subject)
    if not (id or units or subject):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('/home/jimmycooks/sqlite/cool.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run(host="0.0.0.0", port=8080, debug=True)

#app.run(port = 8080)