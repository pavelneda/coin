from django.contrib import admin

from account.models import Card
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone', 'card')
    list_display_links = ('username', 'first_name', 'last_name', 'phone', 'card')


search_fields = ('username', 'first_name', 'last_name', 'phone', 'card')


class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'balance')
    list_display_links = ('number', 'balance')
    search_fields = ['number']


admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
