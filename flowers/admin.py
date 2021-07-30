# imports
from django.contrib import admin

from root import base_classes as base_classes
from flowers import models as flower_models
# End: imports -----------------------------------------------------------------

class FlowerAdmin(base_classes.CustomBaseAdmin):
    list_display = []
    ordering = ['created']
    list_filter = []
    filter_horizontal = []
    search_fields = []


admin.site.register(flower_models.Flower, FlowerAdmin)

