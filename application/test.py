import json
import httplib2
   
sock = httplib2.Http()
sock.add_credentials('admin', 'password') # use basic auth
httplib2.debuglevel = 20
   
message = {"room_id":5, 
           "event_time":1234567820,
           "occupancy":0.75,
           "time":"2016-7-23 16:00:00",
           "reporter":"admin",
           "building":"school of hard knocks"}
 
msg_json = json.dumps(message)
  
print(msg_json)  
headers, resp = sock.request('http://localhost:5000/api/survey/', 'POST', body=msg_json)
print (headers['status'])

 

# print(response)
  
# headers, resp = sock.request('http://localhost:5000/api/room/', 'GET')
# print (headers['status'])



