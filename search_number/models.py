from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20, unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=40)