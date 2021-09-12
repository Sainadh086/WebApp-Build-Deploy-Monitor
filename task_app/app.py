import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from prometheus_flask_exporter import PrometheusMetrics
import logging


logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")
app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

endpoint_count = metrics.counter("endpoint_count", "Counting the endpoints", labels={
    "endpoint": lambda: request.endpoint
} )


try:
    #connecting a mongodb
    user = os.environ.get('MYAPP_DB_USER')
    password = os.environ.get('MYAPP_DB_PASSWORD')
    host = os.environ.get('MYAPP_DB_HOST')
    port = os.environ.get('MYAPP_DB_PORT')

    db = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/')
    notes = db['app']['notes']
except:
    #db = MongoClient("mongodb://192.168.1.8:27017/")
    redirect('/error')
# lambda function
p_data = lambda x: request.form.get(x)




@app.route("/", methods= ['GET', 'POST'])
@endpoint_count
def index():
    if request.method == "POST":
        title = p_data('title')
        desc = p_data('description')
        status = p_data('status')
        operation = p_data('operation')
        id = p_data('id')
        if operation == 'create':
            notes.insert({'title':title, 'description':desc, 'status':status})
        elif operation == 'update':
            notes.update_one({'_id':ObjectId(id)},{'$set' :{'title':title,'description':desc,'status':status}})
        elif operation == 'remove':
            print("*"*10)
            print(id)
            notes.delete_one({'_id':ObjectId(id)})
        elif operation == 'edit':
            data = notes.find({"_id": ObjectId(id) })
            return render_template('edit.html', note = data[0])
        else:
            pass
    data = notes.find()
    return render_template("index.html",notes=data)

@app.route("/create")
@endpoint_count
def create():
    return render_template("create.html")

@app.route("/error")
@endpoint_count
def error():
    return """
    <CENTER><h2> Please enter database credentials </h2><br><H3>Enter Below Details
    <br> MYAPP_DB_USER<br>MYAPP_DB_PASSWORD<BR>
    MYAPP_DB_HOST<BR>
    MYAPP_DB_PORT</H3>
    <CENTER>
    """
if __name__ =="__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)

