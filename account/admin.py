from django.contrib import admin

from account.models import Card
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone')
    list_display_links = ('username', 'first_name', 'last_name', 'phone')


search_fields = ('username', 'first_name', 'last_name', 'phone')


class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'balance', 'user')
    list_display_links = ('number', 'balance', 'user')
    search_fields = ['number']


admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
