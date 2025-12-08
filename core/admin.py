from django.contrib import admin
from .models import Contact, Feedback

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'project_type', 'call_count', 'created_at')
    list_filter = ('project_type', 'preferred_time', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)

    def call_count(self, obj):
        return Contact.objects.filter(name=obj.name).count()
    call_count.short_description = 'Number of Requests'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
