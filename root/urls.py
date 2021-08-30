# imports
import debug_toolbar

from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect, get_object_or_404


# End: imports -----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('bibliotek/', include('library.urls')),
    path('', lambda x: redirect('library:index')),
    
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

