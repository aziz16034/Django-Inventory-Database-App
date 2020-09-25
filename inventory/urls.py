from django.conf.urls import url
from .views import *
from.forms import*
from.models import*

urlpatterns =[

    url(r'^$', index, name='index'),
    url(r'^display_laptops$',display_laptops, name='display_laptops'  ),
    url(r'^display_mobiles$',display_mobiles, name='display_mobiles'  ),
    url(r'^display_phones$',display_phone, name='display_phones'  ),
    url(r'^add_laptop$', add_laptop, name= 'add_laptop'),
    url(r'^add_Mobile$', add_Mobile, name= 'add_Mobile'),
    url(r'^add_phone$', add_phone, name= 'add_phone'),
    url(r'^edit_Laptop/(?P<pk>\d+)$', edit_Laptop, name= 'edit_Laptop'),

    url(r'^edit_Mobile/(?P<pk>\d+)$', edit_Mobile, name= 'edit_Mobile'),
    url(r'^edit_phone/(?P<pk>\d+)$', edit_phone, name= 'edit_phone'),
    url(r'^delete_Laptop/(?P<pk>\d+)$', delete_Laptop, name= 'delete_Laptop'),
    url(r'^delete_Mobile/(?P<pk>\d+)$', delete_Mobile, name= 'delete_Mobile'),
    url(r'^delete_phone/(?P<pk>\d+)$', delete_phone, name= 'delete_phone'),

    








]