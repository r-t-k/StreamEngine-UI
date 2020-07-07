from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Channel

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomCreateChannelForm():

    class Meta:
        model = Channel
        fields = ('title', 'slug', 'vods')

class CustomChangeChannelForm():

    class Meta:
        model = Channel
        fields = ('title', 'slug', 'vods')