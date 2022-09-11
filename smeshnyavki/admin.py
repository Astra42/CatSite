from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class SmeshnyavkаAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_time', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'pub_time')
    prepopulated_fields = {"slug": ("title",)}
    #порядок отображения редактируемых полей
    fields = ('title', 'slug', 'categ', 'content', 'photo', 'get_html_photo', 'is_published', 'pub_time')
    readonly_fields = ('pub_time', 'get_html_photo')
    save_on_top = True
    def get_html_photo(self, object):#mark_safe does'nt screen tags
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


admin.site.register(Smeshnyavkа, SmeshnyavkаAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.site_header = "Святая святых, админ-панель сайта про котиков"
admin.site.site_title = "Админка"
