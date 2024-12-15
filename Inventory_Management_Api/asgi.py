import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('Django_Settings_Module', 'inventory_management_system.settings')

application = get_asgi_application()
