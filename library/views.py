# imports
from django.views import View
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q, Avg, Count, Min, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model; User = get_user_model()
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test

from library import forms as library_forms
from library import models as library_models
# End: imports -----------------------------------------------------------------

class AllFlowersView(View):
    template = "library/all_flowers.html"

    def get(self, request, *args, **kwargs):
        flowers = flower_models.Flower.objects.all()
        return render(request, self.template, {'flowers': flowers})
    

perms_flower_form = [
    # login_required,
]
@method_decorator(perms_flower_form, name='dispatch')
class FlowerFormView(View):
    template = "library/flower_form.html"
    form_class = library_forms.FlowerForm

    def get(self, request, flower_id=None):
        flower = None
        if flower_id:
            flower = get_object_or_404(flower_models.Flower, id=flower_id)
            
        form = self.form_class(instance=flower)
        return render(request, self.template, {'form': form})

    def post(self, request, flower_id=None):
        flower = None
        if flower_id:
            flower = get_object_or_404(flower_models.Flower, id=flower_id)
            
        form = self.form_class(request.POST, request.FILES, instance=flower)
        if form.is_valid():
            flower = form.save(user=request.user) 
            messages.success(request, "Blomst lagret")
            return redirect('flowers:index')
        return render(request, self.template, {'form': form})


class AllBooksView(View):
    template = "library/all_books.html"
    filter_form = library_forms.BookFilterForm

    def get(self, request, *args, **kwargs):
        filter_form = self.filter_form()
        books = library_models.Book.objects.all()
        return render(request, self.template, {'books': books, 'filter_form': filter_form})
    
    def post(self, request, *args, **kwargs):
        filter_form = self.filter_form(request.POST)
        books = library_models.Book.objects.all()
        if filter_form.is_valid():
            books = filter_form.filter(books)
        show_filter = not filter_form.is_empty()
        return render(request, self.template, {
            'books': books,
            'filter_form': filter_form, 
            'show_filter': show_filter,
        })
    

perms_library_form = [
    # login_required,
]
@method_decorator(perms_library_form, name='dispatch')
class BookFormView(View):
    template = "library/book_form.html"
    form_class = library_forms.BookForm

    def get(self, request, book_id=None):
        library = None
        if book_id:
            library = get_object_or_404(library_models.Book, id=book_id)
            
        form = self.form_class(instance=library)
        return render(request, self.template, {'form': form})

    def post(self, request, book_id=None):
        library = None
        if book_id:
            library = get_object_or_404(library_models.Book, id=book_id)
            
        form = self.form_class(request.POST, request.FILES, instance=library)
        if form.is_valid():
            library = form.save(user=request.user or None) 
            messages.success(request, "Bok lagret")
            return redirect('library:view_all_books')
        return render(request, self.template, {'form': form})


