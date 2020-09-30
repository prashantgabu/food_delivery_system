from django.urls import path
from . import views
urlpatterns = [
    path('', views.buyer_dashboard, name='buyer_dashboard'),
    path('buyer_register', views.buyer_register, name='buyer_register'),
    path('buyer_login', views.buyer_login, name='buyer_login'),
    path('buyer_logout', views.buyer_logout, name='buyer_logout'),
    path('buyer_viewDishByCuisine/<int:id>', views.buyer_viewDishByCuisine, name='buyer_viewDishByCuisine'),
    path('buyer_viewDishByRestaurant/<int:id>', views.buyer_viewDishByRestaurant, name='buyer_viewDishByRestaurant'),
    path('buyer_viewDish', views.buyer_viewDish, name='buyer_viewDish'),
    path('buyer_viewDiscount', views.buyer_viewDiscount, name='buyer_viewDiscount'),
    path('buyer_addToCart', views.buyer_addToCart, name='buyer_addToCart'),
    path('buyer_viewCart', views.buyer_viewCart, name='buyer_viewCart'),
    path('buyer_removeDish/<int:id>', views.buyer_removeDish, name='buyer_removeDish'),
    path('buyer_feedback', views.buyer_feedback, name='buyer_feedback'),
    path('buyer_payment', views.buyer_payment, name='buyer_payment'),
    path('buyer_addOnlineOrder', views.buyer_addOnlineOrder, name='buyer_addOnlineOrder'),
    path('buyer_addOfflineOrder', views.buyer_addOfflineOrder, name='buyer_addOfflineOrder'),
    path('buyer_thankyou', views.buyer_thankyou, name='buyer_thankyou'),
    path('handlerequest', views.handlerequest, name='handlerequest'),
    path('buyer_trackOrder', views.buyer_trackOrder, name='buyer_trackOrder'),

]