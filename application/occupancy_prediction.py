from myapp import app
import pymysql
import pandas as pd
from model_functions import dataframe_epochtime_to_datetime

def get_occupancy_json(rid, date, month, year):
    print("gothere")
    #Connect to database
    configdb = app.config['DATABASE']
    
    conn = pymysql.connect(db = 'wifi_db',
                           host = configdb['host'],
                          user = configdb['user'],
                          password =configdb['password']
                          )
    #JACK: The request that sends back all the data for all rooms
    #is taking a bit of time on the client side so I'm going to edit 
    #this SQL query to only include specific information for the time being

    #wifi_logs = pd.read_sql('select * from wifi_log;', con=conn)

    wifi_logs = pd.read_sql('''
        SELECT logd.room_id, logd.event_time, auth_devices, assoc_devices, logd.building, occupancy FROM wifi_db.wifi_log AS logd, wifi_db.survey AS survey 
        WHERE logd.room_id = %s 
            AND FROM_UNIXTIME(logd.event_time, "%%e") = %s 
            AND FROM_UNIXTIME(logd.event_time, "%%m") = %s
            AND FROM_UNIXTIME(logd.event_time, "%%Y") = %s
            AND FROM_UNIXTIME(logd.event_time, "%%e") = FROM_UNIXTIME(survey.event_time, "%%e")
            AND FROM_UNIXTIME(logd.event_time, "%%m") = FROM_UNIXTIME(survey.event_time, "%%m")
            AND FROM_UNIXTIME(logd.event_time, "%%H") = FROM_UNIXTIME(survey.event_time, "%%H");''', con=conn, params=[rid, date, month, year])
    print(wifi_logs)
    room_data = pd.read_sql('select * from room;', con=conn)
    predict_coef = 0.884521 #at a later stage,this will be imported from the db
    
    #Convert epoch to datetime in dataframe
    wifi_logs = dataframe_epochtime_to_datetime(wifi_logs, "event_time")

    wifi_logs = wifi_logs.groupby(['building','room_id', 'event_day', 'event_hour', 'event_month', 'event_year'], 
                                  as_index=False).median()

    #Calculate predicted occupancy
    wifi_logs['occupancy_pred'] = None
    for i in range(wifi_logs.shape[0]):
        wifi_logs.set_value(i, 'occupancy_pred', 
                            wifi_logs['auth_devices'][i] * predict_coef)
    
    #add categories
    wifi_logs['occupancy_category_5'] = None
    wifi_logs['occupancty_category_3'] = None
    wifi_logs['binary_occupancy'] = None

    for i in range(wifi_logs.shape[0]):
        room = wifi_logs['room_id'][i]
        building = wifi_logs['building'][i]

        capacity = room_data['room_cap'].loc[(room_data['room_num'] == room) & (room_data['building'] == building)].values[0]
        
        prediction = set_occupancy_category(wifi_logs['occupancy_pred'][i], capacity)
        
        wifi_logs.set_value(i, 'occupancy_category_5', prediction[0])
        wifi_logs.set_value(i, 'occupancty_category_3', prediction[1])
        wifi_logs.set_value(i, 'binary_occupancy', prediction[2])
    
    wifi_logs_merged = wifi_logs[['building', 
                           'room_id', 
                           'assoc_devices',
                           'event_day', 
                           'event_hour', 
                           'event_month', 
                           'event_year', 
                           'occupancy',
                           'occupancy_category_5', 
                           'occupancty_category_3',
                           'binary_occupancy']]

    #Select only day hours to avoid useless (night / closing hour) data
    #In the future every building's row should be cross checked to ensure that the hours removed are its own opening/closing hours
    #Since we have only 1 building we took its own opening/closing hours
    wifi_logs_merged = wifi_logs_merged[(wifi_logs_merged.event_hour > 8) & (wifi_logs_merged.event_hour < 18)]
    wifi_logs_merged = wifi_logs_merged.reset_index()

    #orient='index' will create 1 json object for each row as opposed to for each column.
    wifi_logs_merged = wifi_logs_merged.to_json(orient='index')
    
    return wifi_logs_merged
       
def set_occupancy_category(occupants, capacity):
    '''function that converts linear predictions to a defined category.
    
    Parameters
    ----------
    occupants: the number of occupants (real or predicted)
    capacity: the room capacity
    
    Returns
    ---------
    list with 3 values:
        at position 0, the occupancy with 5 cateories
        at position 1, the occupancy with 3 categories
        at position 2, the binary occupancy
    
    '''
    
    ratio = occupants/capacity
    
    # assign category based on ratio
    if ratio < 0.125:
        cat5 = 0.0
    elif ratio < 0.375:
        cat5 =  0.25
    elif ratio < 0.625:
        cat5 =  0.5
    elif ratio < 0.875:
        cat5 =  0.75
    else:
        cat5 =  1.0
    
    cat3 = "empty" if cat5 < 0.25 else "moderate" if cat5 < 0.75 else "full" if cat5>= 0.75 else "ERROR"
    
    cat2 = False if cat3 == "empty" else True
    
    return cat5, cat3, cat2 #This will return a tuple

    
if __name__ == "__main__":
    get_occupancy_json()
    print(get_occupancy_json())
