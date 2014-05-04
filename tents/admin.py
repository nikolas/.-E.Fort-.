from django.contrib import admin

from tents.models import Thumper, Spool

class ThumperInline(admin.TabularInline):
    model = Thumper


class SpoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']})
    ]
    inlines = [ThumperInline]
    list_display = ['subject']
    search_fields = ['subject']


admin.site.register(Spool, SpoolAdmin)
