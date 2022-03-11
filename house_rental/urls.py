"""house_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import review_submit

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('frontpage/', views.frontpage, name='frontpage'),
                  path('', views.index, name='index'),
                  path('regform/', views.reg_form, name='regform'),
                  path('houseinfo/', views.houseinfo, name='houseinfo'),
                  path('login/', views.login_form, name='login'),
                  path('logout/', views.logout_form, name='logout'),
                  path('map/', views.mapview, name='map'),
                  path('show-house/', views.show_house, name='show_house'),
                  path('auto_house/', views.auto_house, name='auto_house'),
                  path('details/<int:pk>/', views.house_details, name='details'),
                  path('submit_review/<int:p_id>/', views.submit_review, name='submit_review'),
                  path('dashboard/', views.dashboard, name='dashboard'),
                  path('updatedata/<int:id>/', views.updatedata, name='updatedata'),
                  path('deletedata/<int:id>/', views.deletedata, name='deletedata'),
                  # path('rate_review/', views.rate_review, name='rate_review'),

                  # rating and review's url for js
                  # path('save/<int:pid>', views.save, name='save'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
