# imports
from django.db import models

from root import constants as root_constants
from root import base_classes as base_classes
# End: imports -----------------------------------------------------------------

class Color(base_classes.CustomBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    hex = models.CharField(max_length=6, null=True, blank=True, verbose_name="hex", help_text="Fargekode i hex (6 symboler)")

    class Meta:
        ordering = []
        verbose_name = 'farge'
        verbose_name_plural = 'farger'
        
    def __str__(self):
        return f"{self.name}"
    
    def as_css(self):
        # TODO: handle COLOR_RANDOM
        # if self.name == root_constants.COLOR_RANDOM:
        #     return 
        return f"#{self.hex}"
    

class Domain(base_classes.CustomBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    bg = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='domain_bg', verbose_name='bakgrunnsfarge')
    font = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='domain_font', verbose_name='skriftfarge')
    
    class Meta:
        ordering = []
        verbose_name = 'domene'
        verbose_name_plural = 'domener'
        
    def __str__(self):
        return f"{self.name}"
        
    def color_models_list(self):
        """Hierarchical list of colors from least to most significant"""
        if self.color:
            return [self.color]
        return []
    
    def color_css_list(self):
        return [color.as_css() for color in self.color_models_list()]


class TagGroup(base_classes.CustomBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn')
    domain = models.ForeignKey('root.Domain', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='tag-domene')
    bg = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_group_bg', verbose_name='bakgrunnsfarge')
    font = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_group_font', verbose_name='skriftfarge')
    
    class Meta:
        ordering = []
        verbose_name = 'tag-gruppe'
        verbose_name_plural = 'tag-grupper'
        
    def __str__(self):
        return f"{self.full_name()}"
        
    def full_name(self):
        if self.domain:
            return f"{self.domain.name}:{self.name}"
        return f"{self.name}"
    
    def color_models_list(self):
        """Hierarchical list of colors from least to most significant"""
        colors = []
        if self.domain:
            colors.append( self.domain.color_models_list() )
        if self.color:
            colors.append(self.color)
        return colors
    
    def color_css_list(self):
        return [color.as_css() for color in self.color_models_list()]
        
        
class Tag(base_classes.CustomBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='navn', help_text="En vilkårlig egenskap til en plante. (Tips: Du kan prefikse tags med kolon ':', f.eks. 'familie:fiola' )")
    domain = models.ForeignKey('root.Domain', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='tag-domene')
    group = models.ForeignKey('root.TagGroup', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='tag-gruppe')
    bg = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_bg', verbose_name='bakgrunnsfarge')
    font = models.ForeignKey('root.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_font', verbose_name='skriftfarge')
    
    class Meta:
        ordering = []
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        
    def __str__(self):
        return f"{self.full_name()}"
        
    def full_name(self):
        if self.group:
            return f"{self.group.name}:{self.name}"
        return f"{self.name}"
    
    @classmethod
    def get_tags_from(cls, group=None, domain=None):
        return cls.objects.filter(group=group, group__domain=domain)
    
    def color_models_list(self):
        """Hierarchical list of colors from least to most significant"""
        colors = []
        if self.group:
            colors.append( self.group.color_models_list() )
        if self.color:
            colors.append(self.color)
        return colors
    
    def color_css_list(self):
        return [color.as_css() for color in self.color_models_list()]
            
    