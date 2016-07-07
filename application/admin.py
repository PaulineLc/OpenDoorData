#admin.py - Where you register models for admin interface
from flask_peewee.admin import Admin, ModelAdmin

from app import app
from auth import auth
from models import User, wifi_log,room,timetable,survey,module


class RoomAdmin(ModelAdmin):
    columns = ('room_num', 'room_cap', 'building',)

    
class ModuleAdmin(ModelAdmin):
    columns = ('module_code','instructor')

    
class WifiAdmin(ModelAdmin):
    columns = ('room_id', 'event_time', 'assoc_devices','auth_devices','building')
    foreign_key_lookups = {'room_id': 'room_num'}
    filter_fields = ('room_id', 'event_time', 'assoc_devices','auth_devices', 'building')

   
class TimetableAdmin(ModelAdmin):
    columns = ('room_id', 'mod_code', 'event_time','reg_stu','building')
    foreign_key_lookups = {'mod_code': 'module_code'}
    filter_fields = ('room_id', 'event_time','mod_code',"reg_stu","building")

    
class UserAdmin(ModelAdmin):
    columns = ('username', 'email', 'join_date','active','admin')
    filter_fields = ('username', 'email', 'join_date', 'active','admin')


class SurveyAdmin(ModelAdmin):
    columns = ('room_id', 'event_time', 'occupancy','building')
    foreign_key_lookups = {'room_id':'room_num'}
    filter_fields = ('room_id', 'event_time', 'occupancy', 'building')



#importing admin models
admin = Admin(app, auth)
auth.register_admin(admin)
admin.register(User, UserAdmin)
admin.register(room, RoomAdmin)
admin.register(module, ModuleAdmin)
admin.register(wifi_log, WifiAdmin)
admin.register(timetable, TimetableAdmin)
admin.register(survey, SurveyAdmin)

