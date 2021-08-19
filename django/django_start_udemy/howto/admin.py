from django.contrib import admin
from howto.models import Blog, Entry, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Entry)
admin.site.register(Author)