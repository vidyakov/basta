from basta import Basta

from mainapp import main_app
from adminapp import admin_app


application = Basta([main_app, admin_app])
