from django.urls import path
from . import views
urlpatterns = [
    path('', views.buyer_dashboard, name='buyer_dashboard'),
    path('buyer_register', views.buyer_register, name='buyer_register'),
    path('buyer_login', views.buyer_login, name='buyer_login'),

]