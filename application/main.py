#entry point to site

from myapp import app

from auth import *
from admin import admin
from api import api
from models import *
from views import *



admin.setup()
api.setup()
#setting secret key for sessions
# app.secret_key = app.config['SECRET_KEY']

if __name__ == '__main__':
    app.run()