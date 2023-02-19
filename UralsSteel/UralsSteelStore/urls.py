from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:category_id>/', index, name='category_mp'),
    path('services/', services, name='services'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts_ways, name='contacts_ways'),
    path('services/metal_cutting/', metal_cutting, name='metal_cutting'),
    path('shop_catalog/', shop_catalog, name='shop_catalog'),
    path('shop_catalog/<slug:slug_cat>/', shop_catalog, name='shop_catalog_item'),
    path('shop_catalog/<slug:slug_cat>/about_good/<slug:slug_good_name>/', about_good, name='about_good'),
    path('shop_catalog/<slug:slug_cat>/about_good/<slug:slug_good_name>/<slug:current_img>', about_good, name='current_img'),
    path('basket/', basket, name='basket'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('authorisation/', authorisation, name='authorisation')

]