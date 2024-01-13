from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from . import manager

# Create your models here.

class customuser(AbstractBaseUser,PermissionsMixin):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    DOB=models.DateField(null=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','DOB']

    objects=manager.customusermanager()

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.firstname
    
    def get_full_name(self):
        return self.firstname+self.lastname



