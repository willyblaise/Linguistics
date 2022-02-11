import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/injects/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('cool.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM inject;').fetchall()

    return jsonify(all_books)



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

    conn = sqlite3.connect('cool.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
