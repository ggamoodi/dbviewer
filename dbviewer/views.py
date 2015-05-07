from dbviewer import app
from flask import render_template
import pymongo

@app.route('/<db>/')
def index(db):
    connection = pymongo.MongoClient()
    db = connection.get_database(db)
    collections = db.collection_names()
    collections.remove("system.indexes")

    return render_template("index.html", collections=sorted(collections))