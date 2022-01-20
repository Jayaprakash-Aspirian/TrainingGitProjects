from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from School_Creating_Admin.models import MyUser,school_details


class UserAdmin(BaseUserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "joined_date",
        "is_admin",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "joined_date",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


admin.site.register(MyUser, UserAdmin)
admin.site.register(school_details)