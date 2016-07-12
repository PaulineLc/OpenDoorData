#auth.py - The authentication system used to protect access to the admin.

from flask_peewee.auth import Auth  # Login/logout views, etc.

from myapp import app
from models import User, db


auth = Auth(app, db, user_model = User)
