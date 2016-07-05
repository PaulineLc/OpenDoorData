from flask import Flask
from flask import render_template
from src import queries


import os, sys

app = Flask(__name__)
#mysql = MySQL(app)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'summer'

@app.route('/getjson/<rid>/<day>')
def redner_test(rid, day):
	jdata = queries.hourly_average(rid, day)
	return jdata

@app.route('/')
def render():
	#cur.close().
	return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)