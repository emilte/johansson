# imports
from django.apps import AppConfig
from library import constants as library_constants
# End: imports -----------------------------------------------------------------

INIT_DOMAINS = [
    {'name': library_constants.DOMAIN_FLOWERS},
    {'name': library_constants.DOMAIN_BOOKS},
]


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    
    def ready(self):
        from library import signals
        
        # init instances
        from root import models as root_models
        
        for domain in INIT_DOMAINS:
            try:
                d, created = root_models.Domain.objects.get_or_create(name=domain['name'])
                root_models.TagGroup.objects.get_or_create(name='', domain=d)
            except Exception as e:
                print(f"[{__file__}]: {e}")
        
            
            
            
            
