#models.py - Database models for use with your ORM, business logic, etc.
import peewee
import datetime
from flask_peewee.auth import BaseUser

db = peewee.MySQLDatabase('wifi_db', host="localhost", user='root',passwd='summer')

db.connect()
    
    
class BaseModel(peewee.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db
        
class room(BaseModel):
    room_id = peewee.IntegerField(primary_key=True)
    room_cap = peewee.IntegerField()
    building = peewee.CharField(255)
    
class wifi_log(BaseModel):
    room_id = peewee.ForeignKeyField(room, db_column='room_id')
    event_time = peewee.IntegerField()
    assoc_devices = peewee.IntegerField()
    auth_devices = peewee.IntegerField()
    building = peewee.CharField(255)
    
    
class module(BaseModel):
    mod_code = peewee.CharField(50, primary_key=True)
    reg_stu = peewee.IntegerField()


class timetable(BaseModel):
    room_id = peewee.ForeignKeyField(room, db_column='room_id')
    mod_code = peewee.ForeignKeyField(module, db_column='mod_code')
    event_time = peewee.IntegerField()
    
    class Meta:
        primary_key = peewee.CompositeKey('room_id', 'event_time')

class survey(BaseModel):
    room_id = peewee.ForeignKeyField(room, db_column='room_id')
    event_time = peewee.IntegerField()
    occupancy = peewee.DecimalField(constraints=[peewee.Check('occupancy <= 1 AND occupancy >=0')])
    building = peewee.CharField(255)
    
    class Meta:
        primary_key = peewee.CompositeKey('room_id', 'event_time')
        

class User(BaseModel, BaseUser):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField()
    join_date = peewee.DateTimeField(default=datetime.datetime.now)
    active = peewee.BooleanField(default=True)
    admin = peewee.BooleanField(default=False)


db.create_tables([User], safe=True)

if __name__ == "__main__":
    
    User.create(username = "don",
                 password = "summer",
                 email = "donovanjblaine@gmail.com",
                 admin = True
                 )
    user = User.get(User.username == "don")
    user.set_password ("summer")
    user.save()

db.close()
