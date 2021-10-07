from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.base import Model

from .manager import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICE = (
        ('Male','Male'),
        ('Female','Female'),
    )
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICE,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    # @property
    # def is_anonymous(self):
    #     """
    #     Always return False. This is a way of comparing User objects to
    #     anonymous users.
    #     """
    #     return False
    # @property
    # def is_authenticated(self):
    #     return False