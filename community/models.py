from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class topic(models.Model):
    topicname=models.CharField(max_length=50,null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated']

    def __str__(self):
        return self.topicname

class room(models.Model):
    User=get_user_model()
    name=models.CharField(max_length=200)
    roomtopic=models.ForeignKey(topic,on_delete=models.CASCADE)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField(max_length=500,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated']
    
    def __str__(self):
        return self.desc

class message(models.Model):
    User=get_user_model()

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    roomname=models.ForeignKey(room,on_delete=models.CASCADE)
    body=models.TextField(max_length=500,null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated']


    def __str__(self):
        return self.body
    

class reply(models.Model):
    User=get_user_model()

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    roomname=models.ForeignKey(room,on_delete=models.CASCADE)
    threadname=models.ForeignKey(message,on_delete=models.CASCADE)
    body=models.TextField(max_length=500,null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated']

    def __str__(self):
        return self.body


class favs(models.Model):
    User=get_user_model()

    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    movieid=models.IntegerField(null=False)
    moviename=models.CharField(max_length=300)
    dateadded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.moviename
    class Meta:
        ordering=['-dateadded']


    

    