# imports
from django.urls import path, include
from django.contrib import admin

from root import views as root_views
from library import views as library_views
# End: imports -----------------------------------------------------------------

app_name = 'library'

urlpatterns = [
    path('blomar/alle/', library_views.AllFlowersView.as_view(), name='view_all_flowers'),
    path('blomar/blomst/opprett/', library_views.FlowerFormView.as_view(), name='add_flower'),
    path('blomar/blomst/endre/<int:flower_id>/', library_views.FlowerFormView.as_view(), name='change_flower'),
    # path('bok/<int:flower_id>/', library_views.FlowerView.as_view(), name='view_flower'),

    path('bøker/alle/', library_views.AllBooksView.as_view(), name='view_all_books'),
    # path('bøker/bok/<int:book_id>/', library_views.BookView.as_view(), name='view_book'),
    path('bøker/bok/opprett/', library_views.BookFormView.as_view(), name='add_book'),
    path('bøker/bok/endre/<int:book_id>/', library_views.BookFormView.as_view(), name='change_book'),
    
    # path('musikk/album/alle/', library_views.BookView.as_view(), name='view_all_books'),
    # path('musikk/album/<int:book_id>/', library_views.BookView.as_view(), name='view_book'),
    # path('musikk/album/opprett/', library_views.FlowerFormView.as_view(), name='add_book'),
    # path('musikk/album/endre/<int:book_id>/', library_views.FlowerFormView.as_view(), name='change_book'),
    
    path('tag/opprett/', root_views.TagFormView.as_view(template='library/tag_form.html', success_redirect='index'), name='add_tag'),
    path('tag/endre/<int:tag_id>/', root_views.TagFormView.as_view(template='library/tag_form.html', success_redirect='index'), name='change_tag'),
]

