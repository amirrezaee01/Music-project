from django.contrib import admin
from .models import *

# Register your models here.


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'duration')
    
    

admin.site.register(Song, SongAdmin)    