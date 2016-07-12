##admin.py - Where you register models for admin interface
from flask_peewee.admin import Admin, ModelAdmin

from myapp import app
from auth import auth
from models import User, wifi_log,room,timetable,survey,module, wifiStudents

#fyi to make the admin db useable you need to change unicode in the admin flask peewee package to str
class RoomAdmin(ModelAdmin):
    columns = ('id_field','room_num', 'room_cap', 'building',)
   
class ModuleAdmin(ModelAdmin):
    columns = ('module_code','instructor')
    foreign_key_lookups = {'instructor': 'username'}
    filter_exclude = ('instructor__password','instructor__join_date','instructor__')
    filter_fields = ('module_code','instructor__username','instructor__email','instructor__id')
    
class WifiAdmin(ModelAdmin):
    columns = ('room_id', 'time', 'assoc_devices','auth_devices',)
    foreign_key_lookups = {'room_id': 'id_field'}
    filter_fields = ('room_id', 'time', 'assoc_devices','auth_devices',)
   
class TimetableAdmin(ModelAdmin):
    columns = ('room_id', 'mod_code', 'time','reg_stu')
    foreign_key_lookups = {'mod_code': 'module_code','room_id':'id_field'}
    filter_fields = ('room_id', 'time','mod_code',"reg_stu")
  
class UserAdmin(ModelAdmin):
    columns = ('username', 'email', 'join_date','active','admin')
    filter_fields = ('username', 'email', 'join_date', 'active','admin')
    
    def save_model(self, instance, form, adding=True):
        orig_password = instance.password
     
        user = super(UserAdmin, self).save_model(instance, form, adding)
     
        if orig_password != form.password.data:
            user.set_password(form.password.data)
            user.save()
     
        return user


class SurveyAdmin(ModelAdmin):
    columns = ('room_id', 'time', 'occupancy','instructor')
    foreign_key_lookups = {'room_id':'id_field'}
    filter_fields = ('id_field','room_id', 'time', 'occupancy','instructor__username')
    
class wifiStudentsAdmin(ModelAdmin):
    columns = ('room_id','time','occupancy')
    foreign_key_lookups = {'room_id':'id_field'}
    filter_fields = ('room_id', 'time', 'occupancy')



#importing admin models
admin = Admin(app, auth)
auth.register_admin(admin)
admin.register(User, UserAdmin)
admin.register(room, RoomAdmin)
admin.register(module, ModuleAdmin)
admin.register(wifi_log, WifiAdmin)
admin.register(timetable, TimetableAdmin)
admin.register(survey, SurveyAdmin)
admin.register(wifiStudents, wifiStudentsAdmin)

