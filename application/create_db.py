import peewee
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='summer')

c = conn.cursor()
 
c.execute("CREATE DATABASE IF NOT EXISTS wifi_db")

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
    event_time = peewee.DateTimeField()
    assoc_devices = peewee.IntegerField()
    auth_devices = peewee.IntegerField()
    
class module(BaseModel):
    mod_code = peewee.IntegerField(primary_key=True)
    reg_stu = peewee.IntegerField()

class timetable(BaseModel):
    room_id = peewee.ForeignKeyField(room, db_column='room_id')
    mod_code = peewee.ForeignKeyField(module, db_column='mod_code')
    event_time = peewee.DateTimeField()
    
    class Meta:
        primary_key = peewee.CompositeKey('room_id', 'event_time')

class survey(BaseModel):
    room_id = peewee.ForeignKeyField(room, db_column='room_id')
    event_time = peewee.DateTimeField()
    occupancy = peewee.DecimalField(constraints=[peewee.Check('occupancy <= 1 AND occupancy >=0')])
    
    class Meta:
        primary_key = peewee.CompositeKey('room_id', 'event_time')
    
db.create_tables([room, wifi_log,module,timetable,survey], safe=True)

print("The Database should now be available")