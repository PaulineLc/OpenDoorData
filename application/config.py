# config

class Configuration(object):
    DATABASE = {
        'name': 'example.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = 'shhhh'
    
#     Then in any of your files you could just import the app object to gain access to that dictionary. I tend to access that app object by doing from flask import current_app as app then just app.config['MY_SETTING']