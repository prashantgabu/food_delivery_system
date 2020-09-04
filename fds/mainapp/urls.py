from django.urls import path
from . import views
urlpatterns = [
    path('', views.res_login, name='res_login'),
    path('res_register', views.res_register, name='res_register'),
    path('res_dashboard', views.res_dashboard, name='res_dashboard'),
    path('res_addDish', views.res_addDish, name='res_addDish'),
    path('res_viewDish', views.res_viewDish, name='res_viewDish'),

]
