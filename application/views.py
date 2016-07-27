#views.py - Views that handle requests.

from flask import render_template  
from src import json_creator
from src import queries
from myapp import app
from auth import auth
from models import room

from occupancy_prediction import get_occupancy_json


@app.route('/')
def render():
    #cur.close().
    return render_template("building.html")

@app.route('/dashboard/home')
def renderDashboardHome():
        return render_template("dbhome.html")

@app.route('/dashboard/building')
def renderBuildingPage():
    return render_template("building.html")

@app.route('/api/')
def renderapi():
    #cur.close().
    return render_template("api.html")

@app.route('/survey/')
@auth.login_required
def rendersurvey():
    user = auth.get_logged_in_user()
    rooms= room.select()
    #cur.close().
    return render_template("survey.html", 
                           rooms=rooms)

@app.route('/dashboard/room/')
def renderRoomPage():
    return render_template("index.html")


@app.route('/predicted/<rid>/<date>/<month>/<year>')
def returnPrediction(rid, date, month, year):
    print("gotto route")
    json = get_occupancy_json(rid, date, month, year)
    return json

@app.route('/dailyavg/<rid>')
def returnDailyStats(rid):
	daily_averages = queries.daily_average(rid)
	frequency_of_use = queries.frequency_of_use(rid)
	jdata = json_creator.createRoomJson(daily_averages, frequency_of_use)
	print(jdata)
	return jdata
