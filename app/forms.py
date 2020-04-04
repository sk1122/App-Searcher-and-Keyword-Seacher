# Importing Required Libraries
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


import re  # for Validating Form


class GooglePlayStore(forms.Form):
    """ Form to Accept Data for Google Play Store """
    app_id = forms.CharField(label="Enter App",
                             widget=forms.TextInput(attrs={"class": "appearance-none"}))

    def clean_app_id(self):
        """
            Throws Validation Error
            eg.
            if app_id = com.android.chrome, it does not raises exception
            but if app_id = a.b.c, it does raises a exception
         """

        app_id = self.cleaned_data["app_id"]
        pattern = re.compile(r"com.\w+.\w+")

        match = re.search(pattern, app_id)
        if match:
            pass
        else:
            raise forms.ValidationError("App name does not match")

        return app_id


class AppleAppStore(forms.Form):
    """ Form to Accept Data for Apple App Store """
    app_name = forms.CharField(label="App Name", widget=forms.TextInput(
        attrs={'class': 'appearance-none'}))
    app_id = forms.CharField(label="App Id", widget=forms.TextInput(
        attrs={'class': 'appearance-none'}))


class KeyWordFinder(forms.Form):
    """ Form to Accept Data for Seacrching Keywords """
    site_url = forms.CharField(label="Site URL", widget=forms.TextInput(
        attrs={'class': 'appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none'}
    ))


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"}),
            'password1': forms.PasswordInput(attrs={'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"})
        }
