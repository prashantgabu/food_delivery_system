from django.urls import path
from . import views
urlpatterns = [
    path('', views.res_login, name='res_login'),
    path('res_register', views.res_register, name='res_register'),

]
