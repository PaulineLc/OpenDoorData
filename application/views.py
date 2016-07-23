#views.py - Views that handle requests.

from flask import render_template,request  

from myapp import app
from auth import auth
from models import room


@app.route('/')
def render():
    #cur.close().
    return render_template("index.html")

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
                           rooms=rooms,user=user,password = user.password)
    

@app.route('/submission', methods=['POST'])
def addRegion():
    print("I got it!")
    print(request.form['location'])
    
    return render_template("survey.html")
