from django.contrib import admin
from . import models


@admin.action(description="Make the Post Published")
def publish_post(modeladmin, request, queryset):
    queryset.update(status='PB')

@admin.action(description="Make the Post Draft")
def draft_post(modeladmin, request, queryset):
    queryset.update(status='DF')


@admin.register(models.New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publish_time', 'status']
    # list_editable = ['subtitle']
    list_display_links = ['title', 'publish_time']
    list_filter = ['status', 'category']
    prepopulated_fields = {'slug':['title']}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'subtitle', 'body']
    ordering = ['-publish_time']
    actions = [publish_post, draft_post]
    # We don't need to specify these fields explicitly
    exclude = ['created_time', 'publish_time']
    # readonly_fields = ["slug"]


admin.site.register(models.Category)

admin.site.register(models.Tag)

admin.site.register(models.Comment)

admin.site.register(models.Contact)