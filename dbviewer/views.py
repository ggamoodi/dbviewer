from dbviewer import app
from flask import render_template
from flask import request
import pymongo

client = pymongo.MongoClient()

@app.route('/')
def index():
    dbs = client.database_names()

    return render_template("dbs.html", dbs=sorted(dbs))

@app.route('/<db>/')
def get_collections(db):
    collections = client.get_database(db).collection_names()

    return render_template("collections.html", db=db, collections=sorted(collections))

@app.route('/<db>/<collection>/')
def find_form(db, collection):
    collection = client.get_database(db).get_collection(collection)

    return render_template("find_form.html", db=db, collection=collection.name)

@app.route('/<db>/<collection>/find/', methods=['POST'])
def get_data(db, collection):
    collection = client.get_database(db).get_collection(collection)
    key = request.form['key']
    value = request.form['value']
    type = request.form['type']

    if type == "int":
        result = collection.find({key: int(value)})
    else:
        result = collection.find({key: value})

    print({key: value})

    return render_template("result.html", db=db, collection=collection, result=result)