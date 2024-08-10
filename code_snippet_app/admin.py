from django.contrib import admin
from .models import Snippet  

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('language', 'description',  'created_at') 
    search_fields = ('language', 'description')  
    list_filter = ('language', 'created_at')  
    ordering = ('-created_at',) 


