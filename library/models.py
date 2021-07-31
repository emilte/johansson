# imports
from django.db import models

from root import constants as root_constants
from root import base_classes as base_classes
# End: imports -----------------------------------------------------------------

class Book(base_classes.CustomBaseModel):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='titel')
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='författare')
    
    isbn = models.CharField(max_length=200, null=False, blank=False, verbose_name='isbn')
    ranking = models.PositiveSmallIntegerField(verbose_name='betyg')
    publisher = models.CharField(max_length=200, null=False, blank=False, verbose_name='forlag')
    release_date = models.DateTimeField(verbose_name='utgivningsår')
    nationality = models.CharField(max_length=200, null=False, blank=False, verbose_name='nationalitet')
    pages = models.PositiveSmallIntegerField(verbose_name='antal sidor')
    comment = models.TextField(verbose_name='kommentar')
    
    image_url = models.URLField(verbose_name='bilde', null=True, blank=True, help_text="høyre klikk, kopier bildeaddresse, lim inn her")
    
    tags = models.ManyToManyField('root.Tag', blank=True)
    
    class Meta:
        ordering = []
        verbose_name = 'bok'
        verbose_name_plural = 'bøker'
        
    def __str__(self):
        return f"{self.title}"
