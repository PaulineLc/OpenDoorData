#views.py - Views that handle requests.

from flask import render_template  

from myapp import app
from auth import auth
# from models import User


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
    x = auth.get_logged_in_user()
    y = auth.get_logged_in_user()
    #cur.close().
    return render_template("survey.html", newvariable = x, newvariable2 = y)

