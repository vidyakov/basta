from basta import Basta

from mainapp.routes import MAINAPP_ROUTES
from adminapp.routes import ADMIN_ROUTES


ROUTES = {
    **MAINAPP_ROUTES,
    **ADMIN_ROUTES
}


application = Basta(ROUTES)
