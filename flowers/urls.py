# imports
from django.urls import path, include
from django.contrib import admin

from flowers import views as flower_views
# End: imports -----------------------------------------------------------------

app_name = 'flowers'

urlpatterns = [
    path('', flower_views.IndexView.as_view(), name='index'),
]

