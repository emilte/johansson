# imports
import json
from datetime import datetime

from django import forms
from django.db.models import Count, Q
from django.contrib.auth import get_user_model; User = get_user_model()
from django.contrib.admin.widgets import FilteredSelectMultiple

from root import base_classes as base_classes
from flowers import models as flower_models

# End: imports -----------------------------------------------------------------


class BookForm(base_classes.CustomModelForm):

    required_css_class = 'required font-bold'
    field_classes = 'form-control bg-dark-10 text-light border-dark'

    class Meta:
        model = flower_models.Flower
        fields = [
            'title',
            'author',
            'isbn',
            'ranking',
            'publisher',
            'release_date',
            'nationality',
            'pages',
            'comment',
            'image_url',
            'tags',
        ]

        # https://www.jqueryscript.net/form/Bootstrap-4-Multi-Select-BsMultiSelect.html

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': self.field_classes})
            
        # self.fields['file'].widget.attrs.update({'onchange': 'readURL(this);'})
        
        self.fields['tags'].widget.attrs.update({
            'class':'form-control select2-init', # form-control lets select2 calculate correct width
            'data-selectionCssClass': 'bg-dark-10 text-light border-dark',
            'data-placeholder': 'Søk etter tags...',
        })
        # self.fields['tagged_users'].widget.attrs.update({
        #     'class':'form-control select2-init', 
        #     'data-selectionCssClass': 'bg-dark-10 text-light border-dark',
        #     'data-placeholder': 'Søk etter brukere...',
        # })
        # self.fields['tagged_departments'].widget.attrs.update({
        #     'class':'form-control select2-init', 
        #     'data-selectionCssClass': 'bg-dark-10 text-light border-dark',
        #     'data-placeholder': 'Søk etter seksjoner...',
        # })
        # self.fields['undertext'].label = "Beskrivelse"
