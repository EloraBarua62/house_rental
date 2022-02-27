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

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.frontpage, name='frontpage'),
                  path('regform/', views.reg_form, name='regform'),
                  path('houseinfo/', views.houseinfo, name='houseinfo'),
                  path('login/', views.login_form, name='login'),
                  # path('houselist/', views.house_listview, name='houselist'),
                  # path('', search_location, name='location')
                  # path('autosuggest/', views.autosuggest, name='autosuggest'),
                  path('house-search/', views.house_search, name='house_search'),
                  path('show-house/', views.show_house, name='show_house'),
                  path('auto_house/', views.auto_house, name='auto_house'),
                  path('details/<int:pk>/', views.house_details, name='details')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
