# imports
import PIL
import random

from django import template
from django.conf import settings
from django.utils import timezone
from django.templatetags.static import static
from django.contrib.auth.models import Permission

# End: imports -----------------------------------------------------------------

register = template.Library()


# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/
@register.inclusion_tag('library/components/book.html')
def display_book(request, perms, book, **kwargs):
    return {
        'request': request,
        'perms': perms, 
        'book': book, 
        'classes': kwargs.get('classes'),
    }

@register.inclusion_tag('library/components/book_filter_form.html')
def display_book_filter_form(request, perms, form, **kwargs):
    return {
        'request': request,
        'perms': perms, 
        'form': form, 
        'classes': kwargs.get('classes'),
    }

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/

# @register.simple_tag
# def get_image(model, fielname):
#     if not model or not getattr(model, fieldname):
#         return static('/root/img/image-placeholder.png')
#     return getattr(model, fieldname).url

# 
# # https://stackoverflow.com/questions/16348003/displaying-a-timedelta-object-in-a-django-template
# @register.filter()
# def smooth_timedelta(timedeltaobj):
#     """Convert a datetime.timedelta object into Days, Hours, Minutes, Seconds."""
#     if not timedeltaobj:
#         return None
#     secs = timedeltaobj.total_seconds()
#     timetot = ""
#     if secs > 86400: # 60sec * 60min * 24hrs
#         days = secs // 86400
#         timetot += "{} dager".format(int(days))
#         secs = secs - days*86400
# 
#     if secs > 3600:
#         hrs = secs // 3600
#         timetot += " {} timer".format(int(hrs))
#         secs = secs - hrs*3600
# 
#     if secs > 60:
#         mins = secs // 60
#         timetot += " {} minutter".format(int(mins))
#         secs = secs - mins*60
# 
#     if secs > 0:
#         timetot += " {} sekunder".format(int(secs))
#     return timetot
# 

