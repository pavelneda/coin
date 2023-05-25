from django import forms

class DepositForm(forms.Form):
    purpose = forms.CharField(max_length=100)
    total = forms.IntegerField()
    term = forms.IntegerField()
    percent = forms.IntegerField()


