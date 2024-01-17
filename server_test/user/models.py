from django.db import models


class UserManager(models.Manager):
    pass


class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    objects = UserManager()

    def __str__(self):
        return self.name
