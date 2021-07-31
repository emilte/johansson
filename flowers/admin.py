# imports
from django.contrib import admin

from root import base_classes as base_classes
from flowers import models as flower_models
# End: imports -----------------------------------------------------------------

class FlowerAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'water_freq', 'water_freq_unit', 'water_amount', 'water_amount_unit']
    ordering = ['created']
    list_filter = ['tags']
    filter_horizontal = []
    search_fields = ['name', 'name_latin']


admin.site.register(flower_models.Flower, FlowerAdmin)

