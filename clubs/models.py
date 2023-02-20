from django.db import models


class ClubProfile(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
