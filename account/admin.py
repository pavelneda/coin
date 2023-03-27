from django.contrib import admin

from account.models import User, Card

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'phone', 'card', 'deposit', 'credit')
    list_display_links = ('name', 'login', 'phone', 'card', 'deposit', 'credit')
    search_fields = ('name', 'login', 'phone', 'card', 'deposit', 'credit')

class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'balance')
    list_display_links = ('number', 'balance')
    search_fields = ['number']


admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
