from django.contrib import admin

from .models import Note, Summary
admin.site.register(Note)
admin.site.register(Summary)
