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


class IndexView(View):
    template = "library/index.html"

    def get(self, request, *args, **kwargs):
        library = library_models.Book.objects.all()
        return render(request, self.template, {'library': library})
    

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
            messages.success(request, "Blomst endret")
            return redirect('library:index')
        return render(request, self.template, {'form': form})


