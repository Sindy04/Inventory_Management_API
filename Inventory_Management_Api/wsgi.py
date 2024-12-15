import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('Django_Settings_Module', 'inventory_management_system.settings')

application = get_wsgi_application()
