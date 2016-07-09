
import csv
import time as tm
import datetime
from dateutil.parser import parse
import models

#useful for viewing the specific sql queries to debug
import logging
from models import room
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def main():

    def epochtime(x): 
        string = parse(x)
        epoch = int(tm.mktime(string.timetuple()))
        return epoch
    
    def parseName(x):
        inst1 = x.find(">")+2
        inst2 = x.find(">", inst1)
        
        building = x[inst1:inst2-1]
        room = x[inst2+6:]
        
        return (building,room)
    
    models.db.connect()
    models.db.create_tables([models.User,
                             models.room,
                             models.wifi_log,
                             models.module,
                             models.timetable,
                             models.survey,
                             models.wifiStudents], safe=True)
    
    models.room.create(room_num = 2,
                building = "school of computer science",
                room_cap = 90
                )
    models.room.create(room_num = 3,
                building = "school of computer science",
                room_cap = 90
                )
    models.room.create(room_num = 4,
                building = "school of computer science",
                room_cap = 220
                )
    models.User.create(username = "admin",
                 password = "password",
                 email = "donovanjblaine@gmail.com",
                 admin = True
                 )
    user = models.User.get(models.User.username == "admin")
    user.set_password ("password")
    user.save()
    
    file = r"cleaned_data/timetable.csv"
    
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
    
    modlist = []
    for i in range (1, len(mylist)):
        
        if len(mylist[i][3])>1:
            modulecode = mylist[i][3]
            
            if modulecode in modlist:
                continue
            else:
                models.module.create(module_code = modulecode,
                                     instructor = None
                                     )
                           
            modlist.append(modulecode)
            
    for i in range (1, len(mylist)):
         
        roomid = mylist[i][1]
        build = mylist[i][5]
        roomnum = room.get(room.room_num == roomid, room.building == build)
        time1 = int(mylist[i][2])
        reg_stu = mylist[i][4] if mylist[i][4]!= "" else 0
        modulecode = mylist[i][3] if len(mylist[i][3])>1 else None
        models.timetable.create(room_id = roomnum.id_field,
                         mod_code = modulecode,
                         event_time = time1,
                         reg_stu = int(float(reg_stu)),
                         time = datetime.datetime.fromtimestamp(time1)
                         )
                        
    f.close()
     
    file = r"cleaned_data/full.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(len(mylist)):
        roomid = int(parseName(mylist[i][0])[1])
        build = "school of " + parseName(mylist[i][0])[0]
        roomnum = room.get(room.room_num == roomid, room.building == build)
        etime = float(epochtime(mylist[i][1]))
        models.wifi_log.create(room_id = roomnum.id_field,
                            event_time = etime, 
                            assoc_devices = mylist[i][2], 
                            auth_devices = mylist[i][3],
                            time = datetime.datetime.fromtimestamp(etime)
                            )
      
    f.close()
     
    file = r"cleaned_data/survey_data.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(1, len(mylist)):
        roomid = mylist[i][1]
        build = mylist[i][4]
        roomnum = room.get(room.room_num == roomid, room.building == build)
        etime = int(mylist[i][2])
        models.survey.create(room_id = roomnum.id_field,
                        event_time = etime,
                        occupancy = mylist[i][3],
                        time = datetime.datetime.fromtimestamp(etime)
                        )
         
    f.close()
    
    models.db.close()
    print ("The database should now be available")

if __name__ == '__main__':
    main()
