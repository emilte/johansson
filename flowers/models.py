# imports
from django.db import models

from root import constants as root_constants
from root import base_classes as base_classes
# End: imports -----------------------------------------------------------------


class Flower(base_classes.CustomBaseModel):
    
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    name_latin = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    
    longevity = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    longevity_unit = models.CharField(max_length=20, choices=root_constants.TIME_UNIT, default=None, null=True, blank=True, verbose_name="enhet")

    water_freq = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    water_freq_unit = models.CharField(max_length=20, choices=root_constants.TIME_UNIT, default=None, null=True, blank=True, verbose_name="enhet")
    
    water_amount = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    water_amount_unit = models.CharField(max_length=20, choices=root_constants.TIME_UNIT, default=None, null=True, blank=True, verbose_name="enhet")
    
    water_amount_unit = models.CharField(max_length=20, choices=root_constants.TIME_UNIT, default=None, null=True, blank=True, verbose_name="enhet")
    
    tags = models.ManyToManyField('root.Tag')
    
    class Meta:
        ordering = []
        verbose_name = 'blomst'
        verbose_name_plural = 'blomster'
        
    def __str__(self):
        return f"{self.name}"
        
    
        
    