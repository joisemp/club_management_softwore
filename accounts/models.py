
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . user_manager import UserManager
from org.models import OrgProfile


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_org = models.BooleanField(_('is organisation'), default=False)
    is_student = models.BooleanField(_('is student'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    org = models.ForeignKey(OrgProfile, models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)