# imports
from django.urls import path, include
from django.contrib import admin

from root import views as root_views
from library import views as library_views
# End: imports -----------------------------------------------------------------

app_name = 'library'

urlpatterns = [
    path('', library_views.IndexView.as_view(), name='index'),
    path('bok/alle/', library_views.BookView.as_view(), name='view_all_books'),
    # path('bok/<int:book_id>/', library_views.BookView.as_view(), name='view_book'),
    path('bok/opprett/', library_views.FlowerFormView.as_view(), name='add_book'),
    path('bok/endre/<int:book_id>/', library_views.FlowerFormView.as_view(), name='change_book'),
    
    path('tag/opprett/', root_views.TagFormView.as_view(template='library/tag_form.html', success_redirect='library:index'), name='add_tag'),
    path('tag/endre/<int:tag_id>/', root_views.TagFormView.as_view(template='library/tag_form.html', success_redirect='library:index'), name='change_tag'),
]

