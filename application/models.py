#models.py - Database models for use with your ORM, business logic, etc.
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
        return self.room_num
    def __str__(self):
        return str(self.room_num)
    
class wifi_log(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    event_time = peewee.IntegerField()
    assoc_devices = peewee.IntegerField()
    auth_devices = peewee.IntegerField()

  
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
    module_code = peewee.CharField(50, primary_key=True)
    instructor = peewee.ForeignKeyField(User,default='admin', to_field='username', db_column = 'instructor', on_delete='SET DEFAULT')
    
    def __unicode__(self):
        return self.module_code
     
    def __str__(self):
        return str(self.module_code)


class timetable(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    mod_code = peewee.ForeignKeyField(module, default='open', to_field='module_code', db_column='mod_code', on_delete='SET DEFAULT')
    event_time = peewee.IntegerField()
    reg_stu = peewee.IntegerField()
    

class survey(BaseModel):
    id_field = peewee.PrimaryKeyField()
    room_id = peewee.ForeignKeyField(room,to_field='id_field', db_column='room_id', on_delete='CASCADE')
    event_time = peewee.IntegerField()
    occupancy = peewee.DecimalField(constraints=[peewee.Check('occupancy <= 1 AND occupancy >=0')])
    building = peewee.CharField()
    
    class Meta:
        indexes = ((('room_id','event_time'), True),)
        

db.close()




