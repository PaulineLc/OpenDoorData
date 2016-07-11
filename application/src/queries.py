import pymysql
from src import json_creator as jc

def hourly_average(room, day):
	'''Returns a list of the hourly averages of connected devices based on 
	the database information'''
	hourly_data = []
	chosen_day = getDay(day)
	conn = pymysql.connect(host='localhost', user='root', password='summer')
	c = conn.cursor()
	c.execute("""
    SELECT round(avg(assoc_devices)) 
    FROM wifi_db.wifi_log 
    WHERE room_id = 2 AND 
          FROM_UNIXTIME(event_time,"%%w") = %s AND
          FROM_UNIXTIME(event_time,"%%H") >= 08  
          GROUP BY FROM_UNIXTIME(event_time,"%%H")""", (chosen_day,))

	data = c.fetchall()
	for i in data:
		hourly_data.append(str(i[0]))

	json_output = jc.return_json(hourly_data)

	return json_output

	

def getDay(day):
        '''Returns the day of the week as it is represented in SQLite as a string that can be used for comparison'''
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        return days.index(day)

