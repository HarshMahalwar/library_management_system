from django.contrib import admin
from .models import book, Topic, participant

# Register your models here.

admin.site.register(book)
admin.site.register(Topic)
admin.site.register(participant)