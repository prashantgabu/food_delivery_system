from django.urls import path
from . import views
urlpatterns = [
    path('', views.a_login, name='a_login'),
    path('a_dashboard', views.a_dashboard, name='a_dashboard'),
    path('a_viewRestaurant', views.a_viewRestaurant, name='a_viewRestaurant'),
    path('a_restaurantRequest', views.a_restaurantRequest, name='a_restaurantRequest'),
    path('a_viewAgent', views.a_viewAgent, name='a_viewAgent'),
    path('a_agentRequest', views.a_agentRequest, name='a_agentRequest'),
    path('a_newOrder', views.a_newOrder, name='a_newOrder'),
    path('a_ongoingOrder', views.a_ongoingOrder, name='a_ongoingOrder'),
    path('a_completedOrder', views.a_completedOrder, name='a_completedOrder'),
    path('a_addCuisine', views.a_addCuisine, name='a_addCuisine'),
    path('a_viewCuisine', views.a_viewCuisine, name='a_viewCuisine'),
    path('a_editCuisine/<int:id>', views.a_editCuisine, name='a_editCuisine'),
    path('a_updateCuisine/<int:id>', views.a_updateCuisine, name='a_updateCuisine'),
    path('a_deleteCuisine/<int:id>', views.a_deleteCuisine, name='a_deleteCuisine'),
    path('a_foodReport', views.a_foodReport, name='a_foodReport'),
    path('a_agentReport', views.a_agentReport, name='a_agentReport'),
]