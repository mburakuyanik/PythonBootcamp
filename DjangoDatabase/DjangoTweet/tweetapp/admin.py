from django.contrib import admin
from . import models

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fields = ['nickname']

admin.site.register(models.Tweets, TweetAdmin)
