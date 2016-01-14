from django.contrib import admin
from .models import Story, Comment


# Register your models here.

class Story_Admin(admin.ModelAdmin):
    list_display = ('id','user','checked','passed','context','published_date')

class Comment_Admin(admin.ModelAdmin):
    list_display = ('id','user','comment','comment_date')

admin.site.register(Story,Story_Admin)
admin.site.register(Comment,Comment_Admin)