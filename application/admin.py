#admin.py - Where you register models for admin interface
from flask_peewee.admin import Admin, ModelAdmin

from app import app
from auth import auth
from models import User, wifi_log,room,timetable,survey,module


class RoomAdmin(ModelAdmin):
    columns = ('id_field','room_num', 'room_cap', 'building',)

    
class ModuleAdmin(ModelAdmin):
    columns = ('module_code','instructor')

    
class WifiAdmin(ModelAdmin):
    columns = ('room_id', 'event_time', 'assoc_devices','auth_devices',)
    foreign_key_lookups = {'room_id': 'id_field'}
    filter_fields = ('room_id', 'event_time', 'assoc_devices','auth_devices',)

   
class TimetableAdmin(ModelAdmin):
    columns = ('room_id', 'mod_code', 'event_time','reg_stu')
    foreign_key_lookups = {'mod_code': 'module_code'}
    filter_fields = ('room_id', 'event_time','mod_code',"reg_stu")

    
class UserAdmin(ModelAdmin):
    columns = ('username', 'email', 'join_date','active','admin')
    filter_fields = ('username', 'email', 'join_date', 'active','admin')


class SurveyAdmin(ModelAdmin):
    columns = ('room_id', 'event_time', 'occupancy',)
    foreign_key_lookups = {'room_id':'id_field'}
    filter_fields = ('room_id', 'event_time', 'occupancy')



#importing admin models
admin = Admin(app, auth)
auth.register_admin(admin)
admin.register(User, UserAdmin)
admin.register(room, RoomAdmin)
admin.register(module, ModuleAdmin)
admin.register(wifi_log, WifiAdmin)
admin.register(timetable, TimetableAdmin)
admin.register(survey, SurveyAdmin)

