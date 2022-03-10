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
    MY_CHOICES = (
        ('Flat', 'Flat'),
        ('Duplex', 'Duplex'),
        ('Commercial space', 'Commercial space'),
        ('Sublet', 'Sublet')
    )
    # house_id = models.IntegerField(verbose_name='House ID', null=True, blank=True, unique=True)
    house_name = models.CharField(max_length=50, verbose_name='House Name', blank=True, default='')
    size = models.IntegerField(verbose_name='Size', null=True, blank=True)
    total_room = models.IntegerField(verbose_name='No of Room', null=True, blank=True)
    bed = models.IntegerField(verbose_name='No of Bed Room', null=True, blank=True)
    parking_lot = models.BooleanField(verbose_name='Parking Lot', default=False)
    floor = models.CharField(max_length=5, verbose_name='Floor', blank=True)
    location = models.CharField(max_length=250, verbose_name='Location', blank=True)
    price = models.IntegerField(verbose_name='Rent', null=True, blank=True)
    house_image = models.ImageField(verbose_name='Add House Image', null=True, blank=True, upload_to=upload_image)
    user_photo = models.ImageField(verbose_name='User profile picture', null=True, blank=True, upload_to=upload_image)
    nid_front = models.ImageField(verbose_name='NID front picture', null=True, blank=True, upload_to=upload_image)
    nid_back = models.ImageField(verbose_name='NID back picture', null=True, blank=True, upload_to=upload_image)
    House_type = models.CharField(max_length=20, verbose_name='House Type', default=False, choices=MY_CHOICES)

    # house = objects.get(house_id=house_id)
    # house.set_unusable_password()
    # def house_details(self, password=None):
    #     pass

    # USERNAME_FIELD = 'house_id'
    # REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "House Details"
        verbose_name_plural = "House Details"


class AdminHouse(models.Model):
    admin_house_name = models.CharField(max_length=50, verbose_name='House Name', blank=True, default='')
    admin_size = models.IntegerField(verbose_name='Size', null=True, blank=True)
    admin_total_room = models.IntegerField(verbose_name='No of Room', null=True, blank=True)
    admin_bed = models.IntegerField(verbose_name='No of Bed Room', null=True, blank=True)
    admin_parking_lot = models.BooleanField(verbose_name='Parking Lot', default=False)
    admin_floor = models.CharField(max_length=5, verbose_name='Floor', blank=True)
    admin_location = models.CharField(max_length=250, verbose_name='Location', blank=True)
    admin_price = models.IntegerField(verbose_name='Rent', null=True, blank=True)
    admin_house_image = models.ImageField(verbose_name='Add House Image', null=True, blank=True, upload_to=upload_image)
    admin_user_photo = models.ImageField(verbose_name='User profile picture', null=True, blank=True,
                                         upload_to=upload_image)
    admin_nid_front = models.ImageField(verbose_name='NID front picture', null=True, blank=True, upload_to=upload_image)
    admin_nid_back = models.ImageField(verbose_name='NID back picture', null=True, blank=True, upload_to=upload_image)
    admin_house_type = models.CharField(max_length=20, verbose_name='House Type', blank=True)

    class Meta:
        verbose_name = "Admin House Details"
        verbose_name_plural = "Admin House Details"


class HouseRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(HouseDetails, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=750, blank=True)
    rating = models.FloatField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Rating And Review"
        verbose_name_plural = "Ratings And Reviews"


class ShowMap(models.Model):
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address
