from django.contrib import admin
from .models import Client
from django.utils.html import format_html

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "photo_preview")
    search_fields = ("name", "phone")
    list_filter = ("created_at",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" style="border-radius:4px;" />', obj.photo.url)
        return "—"

    photo_preview.short_description = "Foto"

