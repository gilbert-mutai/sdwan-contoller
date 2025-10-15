from django.contrib import admin
from .models import Router,ConfigTemplate,DeploymentJob

@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'role', 'is_active', 'created_at')
    search_fields = ('name', 'ip_address')

@admin.register(ConfigTemplate)
class ConfigTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    

@admin.register(DeploymentJob)
class DeploymentJobAdmin(admin.ModelAdmin):
    list_display = ('router', 'template', 'status', 'created_at')
    list_filter = ('status',)

