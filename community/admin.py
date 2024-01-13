from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import room,topic,message,reply,favs


# Register your models here.

class roomadmin(ModelAdmin):
    model=room
    list_display=['id','name','host','desc','created','updated']
    list_display_links=['name']

class topicadmin(ModelAdmin):
    model=topic
    list_display=['id','topicname','created','updated']
    list_display_links=['topicname']

class messageadmin(ModelAdmin):
    model=message
    list_display=['id','author','roomname','body','created','updated']
    list_display_links=['id']

class replyadmin(ModelAdmin):
    model=reply
    list_display=['id','author','roomname','threadname','body','created','updated']
    list_display_links=['id']

class favsadmin(ModelAdmin):
    model=favs
    list_display=['id','owner','movieid','moviename','dateadded']

admin.site.register(room,roomadmin)
admin.site.register(topic,topicadmin)
admin.site.register(message,messageadmin)
admin.site.register(reply,replyadmin)
admin.site.register(favs,favsadmin)
