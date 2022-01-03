from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_image(self, filename):
    filename = str(datetime.now().year) + '/' + filename
    return filename


# Create your models here.
class User(AbstractUser):
    """Inherit django abtract user model"""
    phoneno = models.CharField(max_length=15, verbose_name='Phone No', blank=True)

    def __str__(self):
        """
        the value returned from this method will be used as the name of the objects of this class
        """
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class HouseDetails(models.Model):
    # password = None
    house_id = models.IntegerField(verbose_name='House ID', null=True, blank=True, unique=True)
    house_name = models.CharField(max_length=50, verbose_name='House Name', blank=True, default='')
    size = models.IntegerField(verbose_name='Size', null=True, blank=True)
    total_room = models.IntegerField(verbose_name='No of Room', null=True, blank=True)
    bed = models.IntegerField(verbose_name='No of Bed Room', null=True, blank=True)
    parking_lot = models.BooleanField(verbose_name='Parking Lot', default=False)
    floor = models.CharField(max_length=5, verbose_name='Floor', blank=True)
    location = models.CharField(max_length=250, verbose_name='Location', blank=True)
    price = models.IntegerField(verbose_name='Rent', null=True, blank=True)
    house_image = models.ImageField(verbose_name='Add House Image', null=True, blank=True, upload_to=upload_image)

    # house = objects.get(house_id=house_id)
    # house.set_unusable_password()
    # def house_details(self, password=None):
    #     pass

    USERNAME_FIELD = 'house_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "House Details"
        verbose_name_plural = "House Details"
