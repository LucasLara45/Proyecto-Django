from django.contrib import admin
from .models import *
from django.utils.html import format_html

from .models import ServiceOrder

@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "service", "status", "created_at", "photo_preview")
    list_filter = ("service", "status", "created_at")
    search_fields = ("user__username", "description")
    ordering = ("-created_at",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" style="border-radius:4px;" />', obj.photo.url)
        return "—"

    photo_preview.short_description = "Foto"
