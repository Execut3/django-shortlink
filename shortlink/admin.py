from django.contrib import admin

from .models import ShortLink


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    search_fields = ['name', 'short_path', 'full_url']
    list_display = (
        'id', 'name', 'short_path', 'full_url',
    )
    list_per_page = 100
