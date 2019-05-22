from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    handle = models.CharField(max_length=50)
    person = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField()
    following = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)

    def __str__(self):
        return self.handle
