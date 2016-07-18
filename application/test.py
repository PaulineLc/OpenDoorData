# import json
# import httplib2
#  
# sock = httplib2.Http()
# sock.add_credentials('admin', 'password') # use basic auth
#  
# message = {'room_id': 5, 'event_time': 100, 'occupancy': 0.50, 'time': '2015-11-02 09:00:00', 'instructor': 1}
# msg_json = json.dumps(message)
# 
#  
# headers, resp = sock.request('http://localhost:5000/api/survey/', 'POST', body=msg_json)
# print (headers['status'])
##models.py - Database models for use with your ORM, business logic, etc.

import models

roomlist = []
buildinglist = []
all_rooms= models.room.select()
for i in range(0,len(all_rooms)):
    print(all_rooms[i].room_num)
    print(all_rooms[i].building)
    roomlist.append(all_rooms[i].room_num)
    buildinglist.append(all_rooms[i].building)
y= (buildinglist,roomlist)
print (y[1])
print(y[0])
# 
# def get_lists(selection):
#     roomlist = []
#     buildinglist = []
#     all_rooms= selection
#     for i in range(0,len(selection)):
#         roomlist.append(i.room_num)
#         buildinglist.append(i.building)
#     return (buildinglist,roomlist)
# 
# 
# 
# x = get_lists(models.room.select())
# print(x[1])
# print(x[0])