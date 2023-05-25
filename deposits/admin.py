from django.contrib import admin

from deposits.models import Deposit

class DepositAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'total', 'term', 'percent', 'data', 'user')
    list_display_links = ('purpose', 'total', 'term', 'percent', 'user')
    search_fields = ('purpose', 'total', 'term', 'percent', 'data', 'user')

admin.site.register(Deposit, DepositAdmin)
