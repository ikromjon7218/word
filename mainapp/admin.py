from django.contrib import admin
from .models import *

# admin.site.register(Book)
# admin.site.register(Amount)
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

@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ('id',)
    # list_editable = ('name',)
    # list_filter = ('unit', "book")
    list_per_page = 100
    search_fields = 'id', 'name', "description"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ('id', "name")
    # list_editable = ('name',)
    # list_filter = ('name', )
    list_per_page = 100
    search_fields = 'id', 'name', 'about'

@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ("id", "amount_number", "acceptance",)
    list_display_links = ('id', "amount_number")
    # list_editable = ('name',)
    # list_filter = ('name', )
    list_per_page = 100
    search_fields = 'id', 'profil__name', 'amount', "language"
