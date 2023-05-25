import datetime
from random import randint

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from account.forms import RegisterUserForm, LoginUserForm
from account.models import Card

from account.forms import TransferForm


def account(request):
    if request.user.is_authenticated:
        return render(request, 'account/account.html')
    else:
        return redirect('signin')


def logout_user(request):
    logout(request)
    return redirect('signin')


def transfer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TransferForm(request.POST)
            if form.is_valid():
                number = form.cleaned_data.get("number")
                sum = form.cleaned_data.get("sum")
                try:
                    card = Card.objects.get(number=number)
                    if request.user.card.balance >= sum and sum > 0:
                        with transaction.atomic():
                            request.user.card.balance -= sum
                            card.balance += sum
                            request.user.card.save()
                            card.save()
                    else:
                        form.add_error("sum", "Not enough money on your balance")
                except:
                    form.add_error("number", "Card does not exist")
            return render(request, 'account/transfer.html', {'form': form})
        form = TransferForm()
        return render(request, 'account/transfer.html', {'form': form})
    else:
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


def ajax_card(request):
    if _is_ajax(request) and request.user.is_authenticated:

        num_of_card, cvv, date = _createcard()
        card_instance = Card.objects.create(number=num_of_card, cvv=cvv, data=date, user=request.user)
        card_instance.save()

        response = {'num_of_card': num_of_card,
                    'cvv': cvv,
                    'date': date}
        return JsonResponse(response)
    else:
        raise Http404


def _createcard():
    num_of_card = '123456'
    cvv = ''
    while len(num_of_card) != 16:
        i = randint(0, 9)
        num_of_card += str(i)
    while len(cvv) != 3:
        i = randint(0, 9)
        cvv += str(i)
    curdate = datetime.datetime.now()
    month = curdate.month
    year = str(curdate.year + 4)
    date = str(month) + '/' + str(year[2:])
    return num_of_card, cvv, date


def _is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
