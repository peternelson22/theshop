from django.db import models

CHOICES_FOR_GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class Item(models.Model):
    brand = models.CharField(max_length=100, blank = True, null =True)
    price = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank= True, null = True )
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    image_home = models.ImageField(upload_to = 'home/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=1, choices=CHOICES_FOR_GENDER)

    def __str__(self):
        return f'{self.brand }-{self.created_at}'
    
    class Meta:
        ordering = ['-created_at']

class Men(models.Model):
    brand = models.CharField(max_length=100, blank = True, null =True)
    price = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank= True, null = True )
    image = models.ImageField(upload_to = 'mens/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.brand }-{self.created_at}'
    
    class Meta:
        ordering = ['-created_at']

class Women(models.Model):
    brand = models.CharField(max_length=100, blank = True, null =True)
    price = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank= True, null = True )
    image = models.ImageField(upload_to = 'womens/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.brand }-{self.created_at}'
    
    class Meta:
        ordering = ['-created_at']







