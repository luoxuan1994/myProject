from django.contrib import admin
# Register your models here.
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message',               {'fields': ['message_text']}),
        ('Author', {'fields': ['message_name']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Support', {'fields': ['support']}),
    ]
    list_display = ('message_text','message_name', 'pub_date')
admin.site.register(Message, MessageAdmin)