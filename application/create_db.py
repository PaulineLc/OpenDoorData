import peewee
import pymysql
import csv
import time
from dateutil.parser import parse

# The below code is useful for debugging. It shows all sql queries being run. 
# import logging
# logger = logging.getLogger('peewee')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

def main():
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
        
    db.create_tables([room, wifi_log,module,timetable,survey], safe=True)
    
    def epochtime(x): 
        string = parse(x)
        epoch = int(time.mktime(string.timetuple()))
        return epoch
    
    def parseName(x):
        inst1 = x.find(">")+2
        inst2 = x.find(">", inst1)
        
        building = x[inst1:inst2-1]
        room = x[inst2+6:]
        
        return (building,room)
     
    room.create(room_id = 2,
                building = "school of computer science",
                room_cap = 90
                )
    room.create(room_id = 3,
                building = "school of computer science",
                room_cap = 90
                )
    room.create(room_id = 4,
                building = "school of computer science",
                room_cap = 220
                )
    
    
    
    file = r"cleaned_data\timetable.csv"
    
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
    
    modlist = []
    for i in range (1, len(mylist)):
        
        modulecode = mylist[i][3] if len(mylist[i][3]) > 1 else "open"
        reg_stu = mylist[i][4] if mylist[i][4]!= "" else 0
        
        
        if modulecode in modlist:
            continue
        else:
            module.create(mod_code = modulecode,
                    reg_stu = int(float(reg_stu))
                    )
            
        modlist.append(modulecode)
    
    for i in range (1, len(mylist)):
         
        roomid = mylist[i][1]
        time = int(mylist[i][2])
        modulecode = mylist[i][3] if len(mylist[i][3]) > 1 else "open"
        timetable.create(room_id = roomid,
                         mod_code = modulecode,
                         event_time = time
                         )
                        
    f.close()
     
    file = r"cleaned_data\full.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(len(mylist)):
        wifi_log.create(room_id = parseName(mylist[i][0])[1],
                            building = "school of " + parseName(mylist[i][0])[0],
                            event_time = epochtime(mylist[i][1]), 
                            assoc_devices = mylist[i][2], 
                            auth_devices = mylist[i][3]
                            )
      
    f.close()
     
    file = r"cleaned_data\survey_data.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(1, len(mylist)): 
        survey.create(room_id = mylist[i][1],
                        building = mylist[i][4],
                        event_time = mylist[i][2],
                        occupancy = mylist[i][3]
                        )
         
    f.close()
    
    db.close()
    print ("The database should now be available")

if __name__ == '__main__':
    main()


