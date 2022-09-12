from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=254)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=254)
#     profile = models.ImageField(upload_to='images/', blank=True, null=True,)
    
#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name
