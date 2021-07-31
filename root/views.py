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

from root import forms as root_forms
# End: imports -----------------------------------------------------------------


class IndexView(View):
    template = "root/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


perms_tag_form = [
    login_required,
]
@method_decorator(perms_tag_form, name='dispatch')
class TagFormView(View):
    template = "root/tag_form.html"
    form_class = root_forms.TagForm
    success_redirect = 'index'

    def get(self, request, tag_id=None):
        tag = None
        if tag_id:
            tag = get_object_or_404(tag_models.Tag, id=tag_id)
            
        form = self.form_class(instance=tag)
        return render(request, self.template, {'form': form})

    def post(self, request, tag_id=None):
        tag = None
        if tag_id:
            tag = get_object_or_404(tag_models.Tag, id=tag_id)
            
        form = self.form_class(request.POST, request.FILES, instance=tag)
        if form.is_valid():
            tag = form.save(user=request.user) 
            messages.success(request, "Tag lagret")
            return redirect(self.success_redirect)
        return render(request, self.template, {'form': form})



