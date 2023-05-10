from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Amount)
# admin.site.register(Word)
# admin.site.register(Soz)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ('id',)
    list_editable = ('name',)
    list_filter = ('unit', "book")
    list_per_page = 100
    search_fields = 'id', 'name'

@admin.register(Soz)
class SozAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "word")
    list_display_links = ('id',)
    list_editable = ('name',)
    list_filter = ('word__unit', "word__book")
    list_per_page = 100
    search_fields = 'id', 'name', 'word__name'
