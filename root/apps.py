# imports
from django.apps import AppConfig

from root import constants as root_constants
# End: imports -----------------------------------------------------------------

INIT_COLORS = [
    {'name': root_constants.COLOR_RANDOM, 'hex': ''},
    {'name': 'red', 'hex': '#FF0000'},
    {'name': 'green', 'hex': '#00FF00'},
    {'name': 'blue', 'hex': '#0000FF'},
    {'name': 'yellow', 'hex': '#FFFF00'},
    {'name': 'black', 'hex': '#000000'},
    {'name': 'white', 'hex': '#FFFFFF'},
    {'name': 'grey', 'hex': '#888888'},
    {'name': 'purple', 'hex': '#FF00FF'},
    {'name': 'orange', 'hex': '#FFAA00'},
]


class RootConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'root'
        
    def ready(self):
        
        # init instances
        try:
            from root import models as root_models
            for color in INIT_COLORS:
                root_models.Color.objects.get_or_create(name=color['name'], hex=color['hex'][1:] or None) # if hex starts with '#' 
                # root_models.Color.objects.get_or_create(name=color['name'], hex=color['hex'] or None)
        except Exception as e:
            print(f"[{__file__}]: {e}")
            pass
        
