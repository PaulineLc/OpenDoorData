
import csv
import time as tm
from dateutil.parser import parse
import models

#useful for viewing the specific sql queries to debug
import logging
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
    models.db.create_tables([models.User,models.room,models.wifi_log,models.module,models.timetable,models.survey], safe=True)
    
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
        
        modulecode = mylist[i][3] if len(mylist[i][3]) > 1 else "open"
        
        if modulecode in modlist:
            continue
        else:
            models.module.create(module_code = modulecode,
                                 instructor = 'admin'
                                 )
                       
        modlist.append(modulecode)
    
    for i in range (1, len(mylist)):
         
        roomid = mylist[i][1]
        time1 = int(mylist[i][2])
        reg_stu = mylist[i][4] if mylist[i][4]!= "" else 0
        modulecode = mylist[i][3] if len(mylist[i][3]) > 1 else "open"
        models.timetable.create(room_id = roomid,
                         mod_code = modulecode,
                         event_time = time1,
                         reg_stu = int(float(reg_stu)),
                         building = 'school of computer science'
                         )
                        
    f.close()
     
    file = r"cleaned_data/full.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(len(mylist)):
        models.wifi_log.create(room_id = parseName(mylist[i][0])[1],
                            building = "school of " + parseName(mylist[i][0])[0],
                            event_time = epochtime(mylist[i][1]), 
                            assoc_devices = mylist[i][2], 
                            auth_devices = mylist[i][3]
                            )
      
    f.close()
     
    file = r"cleaned_data/survey_data.csv"
     
    with open(file, 'r') as f:
        mycsv= csv.reader(f)
        mylist = list(mycsv)
     
    for i in range(1, len(mylist)): 
        models.survey.create(room_id = mylist[i][1],
                        building = mylist[i][4],
                        event_time = mylist[i][2],
                        occupancy = mylist[i][3]
                        )
         
    f.close()
    
    models.db.close()
    print ("The database should now be available")

if __name__ == '__main__':
    main()
