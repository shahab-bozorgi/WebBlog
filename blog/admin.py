from django.contrib import admin
from . import models


class FilteredByTitile(admin.SimpleListFilter):
    title = 'بر اساس کلمات پرتکرار'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('django', 'DJANGO'),
            ('python', 'PYTHON'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'body', 'status', 'show_image')
    list_editable = ('title',)
    list_filter = ('status', 'author', FilteredByTitile)
    search_fields = ('title', 'body')


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)





