from django.contrib import admin
from .models import HomeCarusel, HomeTopic, HomeCategory
# Register your models here.

@admin.register(HomeCarusel, HomeTopic, HomeCategory)
class HomeCaruselAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']