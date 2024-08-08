from django.contrib import admin
from .models import Snippet

class SnippetsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'owner', 'created']
    list_display = ['title', 'owner', 'created']

admin.site.register(Snippet, SnippetsAdmin)
