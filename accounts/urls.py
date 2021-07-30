# imports
from django.urls import path
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from accounts import views as account_views
from accounts import forms as account_forms
# End: imports -----------------------------------------------------------------

app_name = 'accounts' # Necessary for url naming. eg {% url 'accounts:signin' %}

urlpatterns = [
    path('signup/', account_views.SignUpView.as_view(), name='signup'),
    # path('login/', account_views.LoginView.as_view(), name='login'),
    path('login/', auth_account_views.LoginView.as_view(template_name="accounts/login2.html", form_class=account_forms.CustomAuthenticationForm), name='login'),
    path('logout/', account_views.LogoutView.as_view(), name='logout'),
    path('change_password/', account_views.ChangePasswordView.as_view(), name='change_password'),
    path('profile/edit/', account_views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/', account_views.ProfileView.as_view(), name='profile'),

    #path('delete_user/', views.DeleteUserView.as_view(), name="delete_user"),



]
