from django.contrib import admin

from credits.models import Credit

class CreditAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'total', 'term', 'percent', 'data')
    list_display_links = ('purpose', 'total', 'term', 'percent')
    search_fields = ('purpose', 'total', 'term', 'percent', 'data')


admin.site.register(Credit, CreditAdmin)

