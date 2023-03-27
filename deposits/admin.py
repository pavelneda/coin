from django.contrib import admin

from deposits.models import Deposit

class DepositAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'total', 'term', 'percent', 'data')
    list_display_links = ('purpose', 'total', 'term', 'percent')
    search_fields = ('purpose', 'total', 'term', 'percent', 'data')

admin.site.register(Deposit, DepositAdmin)
