from dbviewer import app
from flask import render_template
import pymongo

@app.route('/')
def index():
    connection = pymongo.MongoClient()
    dbs = connection.database_names()

    return render_template("index.html", text=str(dbs))