# -*- coding:utf8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label=_(u'用户名'), )
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label=_(u'密码'), )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        self.user = authenticate(username=username, password=password)

        if self.user is None:
            msg = _(u'错误的用户名或者密码!')

            raise forms.ValidationError(msg)

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        return authenticate(username=username, password=password)
