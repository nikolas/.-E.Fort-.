from django.contrib import admin

from spools.models import Thumper, Spool, SidebarItem

class ThumperInline(admin.TabularInline):
    model = Thumper
    extra = 1


class SidebarItemAdmin(admin.ModelAdmin):
    list_display = ['content', 'position']


class SpoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']})
    ]
    inlines = [ThumperInline]
    list_display = ['subject', 'created_at']
    search_fields = ['subject']


admin.site.register(SidebarItem, SidebarItemAdmin)
admin.site.register(Spool, SpoolAdmin)
