from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Inherit django abtract user model"""

    def __str__(self):
        """
        the value returned from this method will be used as the name of the objects of this class
        """
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
