#admin.py - Where you register models for admin interface
from flask_peewee.admin import Admin, ModelAdmin

from app import app
from auth import auth
from models import User, wifi_log,room,timetable,survey,module


admin = Admin(app, auth)
auth.register_admin(admin)
admin.register(User, ModelAdmin)
admin.register(User)
admin.register(room)
admin.register(module)
admin.register(wifi_log)
admin.register(timetable)
admin.register(survey)

