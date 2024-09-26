from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=False)

    contact_number = models.CharField(max_length=25)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default=MALE)
    profile_photo = models.ImageField(
        upload_to='images/profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    