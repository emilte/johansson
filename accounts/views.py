# imports
import math
from openpyxl import Workbook

from django.views import View
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q, Avg, Count, Min, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model; User = get_user_model()
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test

from accounts import forms as account_forms
from accounts import models as account_models

# End: imports -----------------------------------------------------------------

profile_dec = [

]

@method_decorator(profile_dec, name='dispatch')
class ProfileView(View):
    template = "accounts/profile.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template, {
        })



@method_decorator(profile_dec, name='dispatch')
class EditProfileView(View):
    template = "accounts/edit_profile.html"
    form_class = account_forms.EditUserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f"Profilen din har blitt oppdatert")
            return redirect('accounts:profile')
        else:
            return render(request, self.template, {'form': form})


class SignUpView(View):
    template = "accounts/registration_form.html"
    form_class = account_forms.SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            try:
                code = form.cleaned_data['code']
                group = account_models.PermissionCode.objects.get(secret=code).group
                user.groups.add(group)
                messages.add_message(request, messages.SUCCESS, f"Med koden '{code}' har du blitt lagt til i avdeling: {group.name}")
            except:
                messages.add_message(request, messages.INFO, f"Koden '{code}' tilsvarer ingen avdeling. Ta kontakt med admin")

            return redirect('home')
        else:
            return render(request, self.template, {'form': form})




@method_decorator(profile_dec, name='dispatch')
class DeleteUserView(View):

    def get(self, request, *args, **kwargs):
        request.user.delete()
        logout(request)
        messages.add_message(request, messages.SUCCESS, f"Brukeren din har blitt slettet fra systemet")
        return redirect('home')


# Should use built in template AuthenticationForm
class LoginView(View):
    template = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        error = None
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            error = "Feil"

        return render(request, self.template, {'error': error})

@method_decorator(profile_dec, name='dispatch')
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


@method_decorator(profile_dec, name='dispatch')
class ChangePasswordView(View):
    template = "accounts/change_password.html"
    form_class = account_forms.CustomPasswordChangeForm
    #form_class = PasswordChangeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, request=request)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Important!
            return redirect("accounts:profile")
        return render(request, self.template, {'form': form})
