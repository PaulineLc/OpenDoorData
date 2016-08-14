#views.py - Views that handle requests.
from flask import render_template, redirect, url_for
from src import json_creator
from src import queries
from app import app
from auth import auth
from models import room,module
import json
from occupancy_prediction import getHistoricalData, getOccupancyRating, getGeneralData, getModuleData,full_room_json,total_full_json

@app.route('/')
def renderHome_Page():
    return render_template("index.html")

# def renderHome_Page():
#     rooms= room.select()
#     data = total_full_json()
#     jsonData = json.dumps(data)
#     return render_template("home.html",
#                            rooms = rooms,
#                            )
@app.route('/api/')
def renderApi():
    return render_template("api.html")

@app.route('/api/occupancy/<rid>/')
def returnFull_Room(rid):
    data = full_room_json(rid)
    jsonData = json.dumps(data)
    return render_template("json_template.html", jsonData = jsonData)

@app.route('/api/occupancy/')
def returnTotalJson():
    data = total_full_json()
    jsonData = json.dumps(data)
    return render_template("json_template.html", jsonData = jsonData)

@app.route('/survey/')
@auth.login_required
def rendersurvey():
    user = auth.get_logged_in_user().username
    rooms= room.select()
    modules = module.select().where(module.instructor == user).order_by(module.module_code)
    return render_template("survey.html", 
                           rooms=rooms,
                           user = user, 
                           modules = modules)

@app.route('/dashboard/')
def renderHome():
    return redirect(url_for('renderDashboardHome'))

@app.route('/dashboard/home')
def renderDashboardHome():
    return render_template("dbhome.html")

@app.route('/dashboard/building')
def renderBuildingPage():
    return render_template("building_test.html")

@app.route('/getBuildingInfo/<bid>')
def getBuldingInfo(bid):
    binfo = queries.getBuildingInfo(bid)
    brinfo = queries.getBuildingRoomInfo(bid)
    building_json = json_creator.createBuildingInfoJson(binfo, brinfo)
    return building_json

@app.route('/dashboard/room/')
def renderRoomPage():
    return render_template("room_test.html")

@app.route('/predicted/<rid>/<date>/<month>/<year>')
def returnPrediction(rid, date, month, year):
    j = getHistoricalData(rid, date, month, year)
    r = json.dumps(j)
    return r

@app.route('/dailyavg/<rid>')
def returnDailyStats(rid):

    #return a python dictionary of the average hourly predicted information for the selected room
    hourly_predictions = getGeneralData(rid)

    #then get information about the frequency of use of the particular room selected
    frequency_of_use_data = queries.frequency_of_use(rid)

    #then get the occupancy rating
    occupancy_rating = getOccupancyRating(rid)
    print(occupancy_rating)
    #combine them into one python dictionary and return as a JSON file to be manipulated using Javascript
    general_data_json = json_creator.createGeneralDataJson(hourly_predictions, frequency_of_use_data, occupancy_rating)


    return general_data_json

@app.route('/dashboard/modules')
def renderModules():
    #need to get the list of all the modules that are on record
    module_list = queries.getModuleList()
    print(module_list)
    return render_template('modules.html', modules=module_list)

@app.route('/getModuleInfo/<mid>')
def getModuleInfo(mid):
    #Get the general module data
    m_data = getModuleData(mid)

    #Get the capacity of the module chosen for calculations on client side
    m_capacity = queries.getModuleCapacity(mid)

    #Merge both module information variables into one JSON file and return
    m_full = json_creator.returnModuleJSON(m_data, m_capacity)
    return m_full

