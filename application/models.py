#models.py - Database models for use with your ORM, business logic, etc.
import peewee

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
    
    class Meta:
        primary_key = peewee.CompositeKey('room_id', 'event_time')
    
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
        
x = room.get(room.room_id == 4).room_cap

print(x)