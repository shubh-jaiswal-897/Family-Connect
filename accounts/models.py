from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PARENT', 'Parent'),
        ('CHILD', 'Child'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='PARENT')

class Family(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='family')
    family_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
