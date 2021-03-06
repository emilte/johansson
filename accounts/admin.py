# imports
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model; User = get_user_model()
from django.contrib.auth.models import Permission

from root import base_classes
from accounts import models as account_models

# End: imports -----------------------------------------------------------------

# Actions for Admin-site:
def make_normal(modeladmin, request, queryset):
    queryset.update(is_staff=False)
    queryset.update(is_superuser=False)
    make_normal_user.short_description = "Mark selected users as normal users without any permissions"

def make_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=False)
    make_staff.short_description = "Mark selected users as is_staff"

def make_superuser(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=True)
    make_superuser.short_description = "Mark selected users as is_superuser"

class UserAdmin(auth_admin.UserAdmin):
    # User forms
    form = auth_admin.UserChangeForm
    add_form = auth_admin.UserCreationForm # Important!
    change_password_form = auth_admin.AdminPasswordChangeForm

    # Fields shown in user detail: admin/accounts//user/'id'/change
    fieldsets = [
        [None,              {'fields': ['password']}],
        ['Personal info',   {'fields': ['username', 'email', 'first_name', 'last_name'] }],
        ['Permissions',     {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}],
        ['Important dates', {'fields': ['last_login', 'date_joined']}],
    ]
    # No idea what this is for
    # limited_fieldsets = [
    #     [None,              {'fields':   []}],
    #     ['Personal info',   {'fields': []}],
    #     ['Important dates', {'fields': ['last_login', 'date_joined']}],
    # ]
    # # Not sure what this is for
    # add_fieldsets = [
    #     [None, {
    #         'classes': ['wide',],
    #         'fields': ['password1', 'password2']}
    #     ],
    # ]

    list_display = ['username', 'id', 'email', 'first_name', 'last_name', 'gender', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'gender']
    search_fields = ['nickname']
    ordering = []
    readonly_fields = ['last_login', 'date_joined']
    filter_horizontal = ['groups', 'user_permissions']
    actions = [make_normal, make_staff, make_superuser]

admin.site.register(User, UserAdmin)
admin.site.register(Permission)
