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

from flowers import forms as flower_forms
from flowers import models as flower_models
# End: imports -----------------------------------------------------------------


class IndexView(View):
    template = "flowers/index.html"

    def get(self, request, *args, **kwargs):
        flowers = flower_models.Flower.objects.all()
        return render(request, self.template, {'flowers': flowers})
    

perms_flower_form = [
    # login_required,
]
@method_decorator(perms_flower_form, name='dispatch')
class FlowerFormView(View):
    template = "flowers/flower_form.html"
    form_class = flower_forms.FlowerForm

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
            flower = form.save(user=request.user or None) 
            messages.success(request, "Blomst endret")
            return redirect('flowers:index')
        return render(request, self.template, {'form': form})


