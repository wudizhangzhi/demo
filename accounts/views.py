# -*- coding:utf8 -*-

from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404

from .models import *
from .forms import LoginForm



class LoginView(FormView):
    # 哔哩哔哩视频页面
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('bilibili:dashboard')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)

            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

    def _get_redirect_url(self, user):
        pass

    def get_context_data(self, **kwargs):
        context_data = super(LoginView, self).get_context_data(**kwargs)
        return context_data


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('accounts:login'))
