from django import forms
from .models import AudioFile, Note

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        def save(self, commit=True):
            user = super.save().save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user
        

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['file']


class NoteRenameForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title']


class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

