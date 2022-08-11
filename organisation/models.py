from django.db import models
from accounts.models import User

class OrgProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=300)
    org_email = models.EmailField(unique=True)
    org_address1 = models.CharField(max_length=200)
    org_address2 = models.CharField(max_length=200, blank=True, null=True)
    org_address3 = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return(self.org_name)