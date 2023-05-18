from django.contrib import admin
from .models import *

@admin.register(Memorization)
class MemorizationAdmin(admin.ModelAdmin):
    list_display = ("id", 'book')
    list_display_links = ('id', 'book')
    # list_editable = ('name',)
    # list_filter = ('name', )
    list_per_page = 100
    search_fields = 'id', 'book', 'profil__name',
