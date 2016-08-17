#entry point to site
from app import app
from auth import *
from admin import admin
from api import api
from models import *
from views import *
import new_data_cleaning
import new_data_entry


admin.setup()
api.setup()
#new_data_cleaning.main()
#new_data_entry.main()

if __name__ == '__main__':
    app.run()