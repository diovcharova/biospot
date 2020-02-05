from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_name = models.CharField()
    email = models.CharField()
    password = models.CharField()

    def __unicode__(self):
        return u"%s" % self.user
