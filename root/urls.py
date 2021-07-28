# imports
from django.urls import path, include
from django.contrib import admin
# End: imports -----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blomar', include('flowers.urls')),
]

