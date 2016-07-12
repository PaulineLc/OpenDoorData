from flask import Flask
from config import DevelopmentConfig
#you

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#mysql = MySQL(app)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'summer'


