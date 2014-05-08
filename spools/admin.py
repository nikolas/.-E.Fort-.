from django.contrib import admin

from spools.models import Thumper, SidebarItem

class SidebarItemAdmin(admin.ModelAdmin):
    list_display = ['content', 'position']


admin.site.register(SidebarItem, SidebarItemAdmin)
admin.site.register(Thumper)
