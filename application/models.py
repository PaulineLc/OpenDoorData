##models.py - Database models for use with your ORM, business logic, etc.
import peewee
import datetime
from flask_peewee.auth import BaseUser
import pymysql

if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', user='root', password='summer')
    c = conn.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS wifi_db")
    conn.close()


db = peewee.MySQLDatabase('wifi_db', host="localhost", user='root',passwd='summer')

db.connect()
  
    
class BaseModel(peewee.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db
        
class room(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_num = peewee.IntegerField()
    room_cap = peewee.IntegerField()
    building = peewee.CharField()
    
    class Meta:
        indexes = (
                   (('room_num', 'building'), True),
                   )
            
    def __unicode__(self):
        return self.id_field
    def __str__(self):
        return str(self.id_field)
    
class wifi_log(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    event_time = peewee.IntegerField()
    assoc_devices = peewee.IntegerField()
    auth_devices = peewee.IntegerField()
    time = peewee.DateTimeField()
  
    class Meta:
        indexes = ((('room_id','event_time'), True),)
    
class User(BaseModel, BaseUser):
    #need to have auto id for sessions to work
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField()
    join_date = peewee.DateTimeField(default=datetime.datetime.now)
    active = peewee.BooleanField(default=True)
    admin = peewee.BooleanField(default=False)
    
    def __unicode__(self):
        return self.username
       
    def __str__(self):
        return str(self.username)
               
class module(BaseModel):
    module_code = peewee.CharField(primary_key=True)
    instructor = peewee.ForeignKeyField(User, db_column = 'instructor', null=True, on_delete='SET NULL')
    
    def __unicode__(self):
        return self.module_code
      
    def __str__(self):
        return str(self.module_code)


class timetable(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    mod_code = peewee.ForeignKeyField(module, to_field='module_code', db_column='mod_code',null=True, on_delete='SET NULL')
    event_time = peewee.IntegerField()
    reg_stu = peewee.IntegerField()
    time = peewee.DateTimeField()
    
    def __unicode__(self):
        return self.id_field   
    def __str__(self):
        return str(self.id_field) 

class survey(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    event_time = peewee.IntegerField()
    occupancy = peewee.FloatField(constraints=[peewee.Check('occupancy <= 1 AND occupancy >=0')])
    time = peewee.DateTimeField()
    instructor = peewee.ForeignKeyField(User, db_column = 'instructor', null=True,default = 'admin', on_delete='SET DEFAULT')
    

    
    class Meta:
        indexes = ((('room_id','event_time'), True),)
        
class wifiStudents(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    event_time = peewee.IntegerField()
    occupancy = peewee.DecimalField(constraints=[peewee.Check('occupancy <= 1 AND occupancy >=0')])
    time = peewee.DateTimeField()

    class Meta:
        indexes = ((('room_id','event_time'), True),)
        

db.close()




