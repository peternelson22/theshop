from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)

def __str__(self):
    return self.name
class Meta:
    ordering = ['name'] 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default="blankimage.png", upload_to="images/users")
    social_media = models.CharField(max_length=255, null=True, blank=True)

def __str__(self):
    return self.Profile.username
class Meta:
    ordering = ['username']     
