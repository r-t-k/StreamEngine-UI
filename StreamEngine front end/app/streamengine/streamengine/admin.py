from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django import forms

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomChangeChannelForm, CustomCreateChannelForm
from .models import CustomUser, Channel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'uid']

admin.site.register(CustomUser, CustomUserAdmin)


class CustomChannelAdmin(admin.ModelAdmin):
    model = Channel
    list_display = ['title', 'slug', 'vods', 'cid']

admin.site.register(Channel)