from django.contrib import admin

from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'data')
    list_display_links = ['title']
    search_fields = ('title', 'description', 'data')


admin.site.register(Blog, BlogAdmin)
