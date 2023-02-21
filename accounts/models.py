
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . user_manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_org = models.BooleanField(_('is organisation'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    

class OrgProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=300)