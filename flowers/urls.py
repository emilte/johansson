# imports
from django.urls import path, include
from django.contrib import admin

from flowers import views as flower_views
from root import views as root_views
# End: imports -----------------------------------------------------------------

app_name = 'flowers'

urlpatterns = [
    path('', flower_views.IndexView.as_view(), name='index'),
    path('blomst/opprett/', flower_views.FlowerFormView.as_view(), name='add_flower'),
    path('blomst/endre/<int:flower_id>/', flower_views.FlowerFormView.as_view(), name='change_flower'),
    path('tag/opprett/', root_views.TagFormView.as_view(template='flowers/tag_form.html', success_redirect='flowers:index'), name='add_tag'),
    path('tag/endre/<int:tag_id>/', root_views.TagFormView.as_view(template='flowers/tag_form.html', success_redirect='flowers:index'), name='change_tag'),
]

