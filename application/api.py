#api.py - Where you register models to be exposed via a REST-ful API

from flask_peewee.rest import RestAPI
from models import room, survey, wifi_log, timetable, module
from app import app # our project's Flask app

# instantiate our api wrapper
api = RestAPI(app)

# register our models so they are exposed via /api/<model>/
api.register(room)
api.register(survey)
api.register(wifi_log)
api.register(timetable)
api.register(module)

# configure the urls
#api.setup()
