##api.py - Where you register models to be exposed via a REST-ful API

from models import room, survey, wifi_log, timetable, module
from myapp import app # our project's Flask app
from auth import auth # import the Auth object used by our project

from flask_peewee.rest import RestAPI,UserAuthentication, RestrictOwnerResource, AdminAuthentication

class SurveyResource(RestrictOwnerResource):
    owner_field = 'reporter'
    
# create an instance of UserAuthentication
user_auth = UserAuthentication(auth)
# instantiate admin-only auth
admin_auth = AdminAuthentication(auth)

# instantiate our api wrapper, specifying user_auth as the default
api = RestAPI(app, default_auth=user_auth)
# register our models so they are exposed via /api/<model>/

api.register(room, auth=admin_auth, allowed_methods=['GET'])
api.register(survey,SurveyResource)
api.register(wifi_log, auth=admin_auth,allowed_methods=['GET'])
api.register(timetable, auth=admin_auth, allowed_methods=['GET'])
api.register(module, auth=admin_auth, allowed_methods=['GET'])

