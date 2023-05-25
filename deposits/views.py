from django.db import transaction
from django.shortcuts import render, redirect

from deposits.forms import DepositForm
from deposits.models import Deposit


def deposits(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = DepositForm(request.POST)

            if form.is_valid():
                total = form.cleaned_data.get("total")
                purpose = form.cleaned_data.get("purpose")
                term = form.cleaned_data.get("term")
                percent = form.cleaned_data.get("percent")

                if not 10 <= percent <= 30:
                    total = -1

                if not 3 <= term <= 24:
                    total = -1

                if request.user.card.balance >= total and total > 0:
                    with transaction.atomic():
                        request.user.card.balance -= total
                        deposit = Deposit.objects.create(total=total, purpose=purpose, term=term, percent=percent,
                                                         user=request.user)
                        deposit.save()
                        request.user.card.save()

                else:
                    form.add_error("total", "Not enough money on your balance")

            return render(request, 'deposits/deposit.html', {'form': form, "deposits": request.user.deposit_set.all()})

        form = DepositForm()
        return render(request, 'deposits/deposit.html', {'form': form, "deposits": request.user.deposit_set.all()})

    else:
        return redirect('signin')
