# imports
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from root import views as root_views
# End: imports -----------------------------------------------------------------

app_name = 'root'

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', root_views.IndexView.as_view(), name='index'),
    path('blomar', include('flowers.urls')),
    # path('blomar', include('flowers.urls', namespace='flowers')),
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)


