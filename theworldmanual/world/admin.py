from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django_json_widget.widgets import JSONEditorWidget

from .models import World, PageTemplate, Page


class WorldAdmin(admin.ModelAdmin):
    list_display = ['title']


class PageTemplateAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon']

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'template', 'world']

    def get_queryset(self, request):
        return super(PageAdmin, self).get_queryset(request).select_related('world', 'template')


admin.site.register(World, WorldAdmin)
admin.site.register(PageTemplate, PageTemplateAdmin)
admin.site.register(Page, PageAdmin)
