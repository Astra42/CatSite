from django.contrib import admin
from .models import *


class SmeshnyavkаAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_time', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'pub_time')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Smeshnyavkа, SmeshnyavkаAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)