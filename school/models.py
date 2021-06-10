from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import uuid

class User(AbstractUser):
    pass

class UserRole(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

def code():
        code = uuid.uuid4().hex[:6].upper()
        return code

class School(models.Model):
    school_name = models.CharField(max_length=255)
    school_id = models.CharField(unique=True, default=code, editable=False, max_length=6)
    profile_admin_name = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    zip = models.IntegerField()
    school_country = CountryField()

    def __str__(self):
        return self.school_name + ' | ' + self.school_id + ' | ' + self.address_line1 + ' | ' + self.State + ' | ' + str(self.school_country)