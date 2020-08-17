from basta.application import BastaWithLogger

from mainapp import main_app
from adminapp import admin_app


application = BastaWithLogger([main_app, admin_app])
