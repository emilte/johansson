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

@register.inclusion_tag('root/components/input_group.html')
def input_group(field, after=False, **kwargs):
    default_classes = "bg-dark-30 text-light border-0"
    return {
        'field': field,
        'after': after,
        'classes': kwargs.get('classes'),
        'default_classes': kwargs.get('default_classes', default_classes),
        'field_classes': kwargs.get('field_classes'),
        'label_classes': kwargs.get('label_classes'),
        'icon_classes': kwargs.get('icon_classes'),
        'error_classes': kwargs.get('error_classes'),
        'prefix': kwargs.get('prefix'),
        'prefix_classes': kwargs.get('prefix_classes'),
        'suffix': kwargs.get('suffix'),
        'suffix_classes': kwargs.get('suffix_classes'),
    }

@register.simple_tag
def get_image(model, fielname):
    if not model or not getattr(model, fieldname):
        return static('/root/img/image-placeholder.png')
    return getattr(model, fieldname).url

@register.simple_tag
def divide(arg1, arg2):
    try:
        return round(int(arg1) / int(arg2), 1)
    except (ValueError, ZeroDivisionError):
        return 0

# use floatformat
# @register.simple_tag
# def round_decimal(number, decimals):
#     if decimals <= 0:
#         return int(number)
#     return round(number, decimals)

@register.simple_tag
def is_dark(color):
    if not color:
        return True
    c_hex = f'#{color}'
    r, g, b = PIL.ImageColor.getcolor(c_hex, "RGB")
    return True if (r+g+b) < 600 else False

@register.simple_tag
def random_choice(iterable):
    return random.choice(iterable)

# settings value
@register.simple_tag(name="get_settings")
def get_settings(var_name):
    """
    Usage:
        {% settings_value "LANGUAGE_CODE" %}
    """
    return getattr(settings, var_name, "")

@register.filter(name='times')
def times(number):
    """Enables in-range for-loops within templates given a number"""
    return range(number)


@register.filter(name="since")
def time_since_datetime(datetime):
    seconds = (timezone.now()-datetime).total_seconds()
    if seconds < 60*2:
        return "Akkurat nå"
    elif seconds < 60*60:
        return f"{int(seconds//60)} minutter siden" 
    elif seconds < 60*60*24:
        return f"{int(seconds//3600)} timer siden" 
    elif seconds < 60*60*24*3: 
        return f"{int(seconds//86400)} dager siden" 
    return datetime

# https://stackoverflow.com/questions/16348003/displaying-a-timedelta-object-in-a-django-template
@register.filter()
def smooth_timedelta(timedeltaobj):
    """Convert a datetime.timedelta object into Days, Hours, Minutes, Seconds."""
    if not timedeltaobj:
        return None
    secs = timedeltaobj.total_seconds()
    timetot = ""
    if secs > 86400: # 60sec * 60min * 24hrs
        days = secs // 86400
        timetot += f"{int(days)} dager"
        secs = secs - days*86400

    if secs > 3600:
        hrs = secs // 3600
        timetot += f" {int(hrs)} timer"
        secs = secs - hrs*3600

    if secs > 60:
        mins = secs // 60
        timetot += f" {int(mins)} minutter"
        secs = secs - mins*60

    if secs > 0:
        timetot += f" {secs} sekunder"
    return timetot
    

