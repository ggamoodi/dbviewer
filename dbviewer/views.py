from dbviewer import app
from flask import render_template
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
def get_data(db, collection):
    collection = client.get_database(db).get_collection(collection)
    result = collection.find().limit(10)

    return render_template("data.html", result=result)