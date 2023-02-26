from django.db import models
from django.conf import settings


class OrgProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.name)