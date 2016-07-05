#api.py - Where you register models to be exposed via a REST-ful API

from flask_peewee.rest import RestAPI
from models import room, survey
from app import app # our project's Flask app

# instantiate our api wrapper
api = RestAPI(app)

# register our models so they are exposed via /api/<model>/
api.register(room)
api.register(survey)

# configure the urls
#api.setup()
