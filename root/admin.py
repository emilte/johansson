# imports
from django.contrib import admin

from root import base_classes
from root import models as root_models
# End: imports -----------------------------------------------------------------

class ColorAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'hex']
    ordering = ['created']
    list_filter = []
    filter_horizontal = []
    search_fields = ['name', 'hex']

class DomainAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'bg', 'font']
    ordering = ['created']
    list_filter = []
    filter_horizontal = []
    search_fields = []

class TagGroupAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'creator', 'created']
    ordering = ['created']
    list_filter = []
    filter_horizontal = []
    search_fields = ['name']

class TagAdmin(base_classes.CustomBaseAdmin):
    list_display = ['name', 'full_name', 'bg', 'font', 'creator', 'created']
    ordering = ['created']
    list_filter = []
    filter_horizontal = []
    search_fields = ['name']


admin.site.register(root_models.Color, ColorAdmin)
admin.site.register(root_models.Domain, DomainAdmin)
admin.site.register(root_models.TagGroup, TagGroupAdmin)
admin.site.register(root_models.Tag, TagAdmin)

