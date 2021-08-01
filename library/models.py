# imports
from django.db import models

from root import constants as root_constants
from root import base_classes as base_classes
# End: imports -----------------------------------------------------------------


class Flower(base_classes.CustomBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    name_latin = models.CharField(max_length=200, null=True, blank=True, verbose_name='latinsk navn')
    
    longevity = models.DecimalField(default=1, decimal_places=1, max_digits=100, null=True, blank=True, verbose_name='levetid')
    longevity_unit = models.CharField(default=root_constants.YEARS, max_length=20, choices=root_constants.TIME_UNITS, null=True, blank=True, verbose_name="enhet")

    water_freq = models.DecimalField(default=7, decimal_places=1, max_digits=100, null=True, blank=True, verbose_name="vannefrekvens")
    water_freq_unit = models.CharField(default=root_constants.DAYS, max_length=20, choices=root_constants.TIME_UNITS, null=True, blank=True, verbose_name="enhet")
    
    water_amount = models.DecimalField(default=2, decimal_places=1, max_digits=100, null=True, blank=True, verbose_name="vannmengde")
    water_amount_unit = models.CharField(default=root_constants.DL, max_length=20, choices=root_constants.VOLUME_UNITS, null=True, blank=True, verbose_name="enhet")
    
    image_url = models.URLField(verbose_name='bilde', null=True, blank=True, help_text="høyre klikk, kopier bildeaddresse, lim inn her")
    # water_amount_unit = models.CharField(max_length=20, choices=root_constants.TIME_UNITS, default=None, null=True, blank=True, verbose_name="enhet")
    
    tags = models.ManyToManyField('root.Tag', blank=True)
    
    class Meta:
        ordering = []
        verbose_name = 'blomst'
        verbose_name_plural = 'blomster'
        
    def __str__(self):
        return f"{self.name}"
        

class Book(base_classes.CustomBaseModel):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='titel')
    author = models.CharField(max_length=200, null=True, blank=True, verbose_name='författare')
    
    isbn = models.CharField(max_length=200, null=True, blank=True, verbose_name='isbn')
    ranking = models.PositiveSmallIntegerField(verbose_name='betyg')
    publisher = models.CharField(max_length=200, null=True, blank=True, verbose_name='forlag')
    release_date = models.DateField(null=True, blank=True, verbose_name='utgivningsår')
    nationality = models.CharField(max_length=200, null=True, blank=True, verbose_name='nationalitet')
    pages = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='antal sidor')
    comment = models.TextField(null=True, blank=True, verbose_name='kommentar')
    
    image_url = models.URLField(null=True, blank=True, verbose_name='bilde', help_text="høyre klikk, kopier bildeaddresse, lim inn her")
    
    tags = models.ManyToManyField('root.Tag', blank=True)
    
    class Meta:
        ordering = []
        verbose_name = 'bok'
        verbose_name_plural = 'bøker'
        
    def __str__(self):
        return f"{self.title}"
