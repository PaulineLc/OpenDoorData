from flask import Flask
from flask import render_template
import create_db
import os, sys

app = Flask(__name__)
#mysql = MySQL(app)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'summer'

@app.route('/test')
def redner_test():
	return render_template("test.html")
@app.route('/')
def render():
	#run intial code to create database and tables
	os.system("create_db.py")
	#create a database cursor
	#cur = mysql.connection.cursor()
	#cur.close()
	return render_template("index.html")

def test():
	return("yo")

if __name__ == '__main__':
    app.run(debug = True)