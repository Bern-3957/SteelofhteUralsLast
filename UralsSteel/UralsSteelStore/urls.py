from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('<int:category_id>/', IndexListView.as_view(), name='category_mp'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about_us/', About_Us_TemplateView.as_view(), name='about_us'),
    path('contacts/', contacts_ways, name='contacts_ways'),
    path('services/metal_cutting/', Metal_cutting_View.as_view(), name='metal_cutting'),
    path('shop_catalog/', ShopCatalog.as_view(), name='shop_catalog'),
    path('shop_catalog/<slug:slug_cat>/', ShopCatalogCategory.as_view(), name='shop_catalog_item'),
    path('shop_catalog/<slug:slug_cat>/about_good/<slug:slug_good_name>/', about_good, name='about_good'),
    path('shop_catalog/<slug:slug_cat>/about_good/<slug:slug_good_name>/<slug:current_img>', about_good, name='current_img'),
    path('basket/', basket, name='basket'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('authorisation/', AuthorisationUser.as_view(), name='authorisation'),
    path('logout/', logout_user, name='logout')

]