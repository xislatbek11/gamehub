from django.contrib import admin
from .models import SystemTool

@admin.register(SystemTool)
class SystemToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'size', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    fields = ('name', 'description', 'version', 'size', 'file', 'screenshot', 'is_active')
