from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegisterUserForm, LoginUserForm


def account(request):
    return render(request, 'account/account.html')


def logout_user(request):
    logout(request)
    return redirect('signin')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('account')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/signin.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('account')
