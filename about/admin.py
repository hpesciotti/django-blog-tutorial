from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'update_on')
    search_fields = ['title']
    # list_filter = ('update_on')
    summernote_fields = ('content')