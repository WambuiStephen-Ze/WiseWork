from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

# app_name = 'umeme'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('starter/', views.starters, name='starter'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('insert/', views.insert, name='insert'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('product/', views.product, name='products'),
    path('team/', views.team, name='team'),
    path('stkpush/', views.stkpush, name='stkpush'),
    path('pay/', views.pay, name='pay'),
    # path('crud/', views.crud, name='crud'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
   path('insert_data/', views.insert_data, name='insert_data'),

    # path('fetch/', views.fetch, name='fetch'),

    path('update_product/<id>', views.update_product, name='update_product'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),
    path('residential/', views.residential, name='residential'),
    path('commercial/', views.commercial, name='commercial'),
    path('industrial/', views.industrial, name='industrial'),
    path('fieldwork/', views.fieldwork, name='fieldwork'),


]