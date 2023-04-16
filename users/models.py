from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.OneToOneField(User, max_length=20, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)

    USERNAME_FIELDS = ('email')
    REQUIRED_FIELDS = ('username')
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/users")
    social_media = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
  
