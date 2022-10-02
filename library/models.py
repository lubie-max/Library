from ast import Str
from distutils.command.upload import upload
from email.policy import default
from enum import auto
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

# class  User(AbstractUser):
#     email_varified = models.BooleanField(default=False)


class Book(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4 , editable= False)

    title = models.CharField(max_length= 200)
    cover = models.ImageField(upload_to= 'cover')
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f' {self.title} - {self.created_at}'
