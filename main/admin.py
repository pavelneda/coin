from django.contrib import admin

from main.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['number']
    list_display_links = ['number']
    search_fields = ['number']


admin.site.register(Department, DepartmentAdmin)

