
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class PlayerManager(models.Manager):

    def create_new(self, user):
        profile = self.create(user=user,
                              name=user.first_name+" "+user.last_name,)

        return profile


@python_2_unicode_compatible
class PlayerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    objects = PlayerManager()

    def create(cls, user, name):
        profile = cls.create(user=user, name=name)
        return profile

    def __str__(self):
        return self.name
