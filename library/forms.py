# imports
import json
from datetime import datetime

from django import forms
from django.db.models import Count, Q
from django.contrib.auth import get_user_model; User = get_user_model()
from django.contrib.admin.widgets import FilteredSelectMultiple

from root import models as root_models
from root import base_classes as base_classes
from library import models as library_models
from library import constants as library_constants

# End: imports -----------------------------------------------------------------


class FlowerForm(base_classes.CustomModelForm):

    required_css_class = 'required font-bold'
    field_classes = 'form-control bg-dark-10 text-light border-dark'

    class Meta:
        model = library_models.Flower
        fields = [
            'name',
            'name_latin',
            'longevity',
            'longevity_unit',
            'water_freq',
            'water_freq_unit',
            'water_amount',
            'water_amount_unit',
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


class BookForm(base_classes.CustomModelForm):

    required_css_class = 'required font-bold'
    field_classes = 'form-control bg-dark-10 text-light border-dark'

    class Meta:
        model = library_models.Book
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
            'class':'select2-init form-control', # form-control lets select2 calculate correct width
            'data-selectionCssClass': 'bg-dark-10 text-light border-dark',
            'data-placeholder': 'Søk etter tags...',
            # 'data-width': '100%',
        })
        
        self.fields['release_date'].widget.attrs.update({
            'class': 'flatpickr-init form-control bg-dark-10 text-light border-dark',
            'autocomplete': 'off',
        })


class BookFilterForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, label="Søk")
    # TODO: test om denne blir evaluert bare en gang?
    ranking = forms.IntegerField(required=False, label="betyg")
    date_from = forms.DateField(required=False, label="dato (fra)")
    date_to = forms.DateField(required=False, label="dato (til)")
    
    pages_from = forms.IntegerField(required=False, label="antal sidor (fra)")
    pages_to = forms.IntegerField(required=False, label="antal sidor (til)")
    
    tags = forms.ModelMultipleChoiceField(required=False, queryset=root_models.Tag.objects.all(), label="Tags")
    
    required_css_class = 'required font-bold'
    field_classes = 'form-control bg-dark-10 text-light border-dark'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': self.field_classes})
            
        # self.fields['file'].widget.attrs.update({'onchange': 'readURL(this);'})
        
        self.fields['search'].widget.attrs.update({
            'placeholder': "Søk etter f.eks. titel, forfatter, nationalitet",
        })
        self.fields['ranking'].widget.attrs.update({
            'placeholder': 'Betyg',
        })
        
        self.fields['date_from'].widget.attrs.update({
            'placeholder': 'Dato (fra)',
        })
        self.fields['date_to'].widget.attrs.update({
            'placeholder': 'Dato (til)',
        })
        self.fields['pages_from'].widget.attrs.update({
            'placeholder': 'Antal sidor (fra)',
        })
        self.fields['pages_to'].widget.attrs.update({
            'placeholder': 'Antal sidor (til)',
        })
        
        self.fields['tags'].widget.attrs.update({
            'class':'select2-init form-control', # form-control lets select2 calculate correct width
            'data-selectionCssClass': 'bg-dark-10 text-light border-dark',
            'data-width': '90%',
            'data-placeholder': 'Søk etter tags...',
        })
        
        self.fields['date_from'].widget.attrs.update({
            'class': 'flatpickr-init form-control bg-dark-10 text-light border-dark',
            'autocomplete': 'off',
        })
        self.fields['date_to'].widget.attrs.update({
            'class': 'flatpickr-init form-control bg-dark-10 text-light border-dark',
            'autocomplete': 'off',
        })
    
    def is_empty(self):
        fields = dict(self.data)
        fields.pop('csrfmiddlewaretoken')
        return all(field == [''] for field in fields.values())
        
    def filter(self, queryset):
        search = self.cleaned_data.get('search', None)
        if search:
            # Making a pretty hardcore filter
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(isbn__icontains=search) |
                Q(nationality__icontains=search) |
                Q(comment__icontains=search)
            ).distinct()
            
        pages_from = self.cleaned_data.get('pages_from') or 0
        queryset = queryset.filter(pages__gte=pages_from)
        pages_to = self.cleaned_data.get('pages_to')
        if pages_to:
            queryset = queryset.filter(pages__lte=pages_to)
            
        date_from = self.cleaned_data.get('date_from')
        date_to = self.cleaned_data.get('date_to')
        if date_from:
            queryset = queryset.filter(release_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(release_date__lte=date_to)
        
        tags = self.cleaned_data.get('tags', None)
        if tags:
            queryset = queryset.filter(tags__in=tags)
        return queryset
