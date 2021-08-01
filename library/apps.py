# imports
from django.apps import AppConfig
from library import constants as library_constants
# End: imports -----------------------------------------------------------------

# DOMAIN_MUSIC = 'musikk'
# DOMAIN_BOOKS = 'bøker'
INIT_DOMAINS = [
{'name': library_constants.DOMAIN_FLOWERS},
# {'name': DOMAIN_MUSIC},
# {'name': DOMAIN_BOOKS},
]

class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    
    def ready(self):
        from library import signals
        
        # init instances
        try:
            from root import models as root_models
            from library import models as flower_models
            
            for domain in INIT_DOMAINS:
                root_models.Domain.objects.get_or_create(name=domain['name'])
        except Exception as e:
            print(f"[{__file__}]: {e}")
            
