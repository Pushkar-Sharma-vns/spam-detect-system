from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["phone", "name"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EditUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "name", "email", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    form = EditUserForm
    add_form = CreateUserForm

    list_display = ["phone", "name", "is_admin", "email", "created_at"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone", "password"]}),
        ("Timestamped", {"fields": ["updated_at"]}),
        ("Personal info", {"fields": ["name", "email"]}),
        ("Active Status", {"fields": ["is_active"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone", "name", "password1", "password2"],
            },
        ),
    ]
    
    search_fields = ["phone", "name"]
    ordering = ["-created_at"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)