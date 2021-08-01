# imports
from django.contrib import admin

from root import base_classes as base_classes
from library import models as library_models
# End: imports -----------------------------------------------------------------


class FlowerAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'water_freq', 'water_freq_unit', 'water_amount', 'water_amount_unit']
    ordering = ['created']
    list_filter = ['tags']
    filter_horizontal = []
    search_fields = ['name', 'name_latin']


class BookAdmin(base_classes.CustomBaseAdmin):
    list_display = ['title', 'author', 'publisher', 'release_date', 'pages', 'ranking']
    ordering = ['created']
    list_filter = ['tags']
    filter_horizontal = []
    search_fields = ['title', 'author']

admin.site.register(library_models.Book, BookAdmin)
admin.site.register(library_models.Flower, FlowerAdmin)

