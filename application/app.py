from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'finaltest'
#mysql.init_app(app)


@app.route('/')
def render():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM candidates''')
	rv = cur.fetchall()
	cur.close()
	return str(rv)

if __name__ == '__main__':
    app.run(debug = True)