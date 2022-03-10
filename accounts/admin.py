from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseDetails)
class HouseDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(AdminHouse)
class AdminHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseRate)
class HouseRateAdmin(admin.ModelAdmin):
    pass


@admin.register(ShowMap)
class ShowMapAdmin(admin.ModelAdmin):
    pass
