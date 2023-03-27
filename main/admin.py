from django.contrib import admin

from main.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['address']
    list_display_links = ['address']
    search_fields = ['address']


admin.site.register(Department, DepartmentAdmin)

