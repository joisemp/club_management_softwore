from django.db import models
from org.models import OrgProfile


class ClubProfile(models.Model):
    org = models.ForeignKey(OrgProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
