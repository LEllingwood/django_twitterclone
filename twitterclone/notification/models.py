from django.db import models


class Notifications(models.Model):
    has_notification = models.BooleanField()


user created the notification for and the tweet 


    def __str__(self):
        return self.name