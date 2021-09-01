# imports
import debug_toolbar

from django.conf import settings
from django.urls import path, include, reverse
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import RedirectView

from library import views as library_views
# End: imports -----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('bibliotek/', include('library.urls')),
    path('brukere/', include('accounts.urls')),
    path('', library_views.IndexView.as_view(), name='index'),
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

