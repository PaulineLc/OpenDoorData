#configuration
    
class Config(object):
    DATABASE = {
        'name': 'wifi_db',
        'host': 'localhost',
        'user': 'root',
        'password': 'summer'
    }
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'shhhh'


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True

