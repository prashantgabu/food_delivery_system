from django.urls import path
from . import views
urlpatterns = [
    path('', views.res_login, name='res_login'),
    path('res_register', views.res_register, name='res_register'),
    path('res_dashboard', views.res_dashboard, name='res_dashboard'),
    path('res_addDish', views.res_addDish, name='res_addDish'),
    path('res_viewDish', views.res_viewDish, name='res_viewDish'),
    path('res_editDish/<int:id>', views.res_editDish, name='res_editDish'),
    path('res_updateDish/<int:id>', views.res_updateDish, name='res_updateDish'),
    path('res_deleteDish/<int:id>', views.res_deleteDish, name='res_deleteDish'),
    path('res_editProfile', views.res_editProfile, name='res_editProfile'),
    path('res_updateProfile', views.res_updateProfile, name='res_updateProfile'),
    path('res_verification', views.res_verification, name='res_verification'),
    path('res_changePassword', views.res_changePassword, name='res_changePassword'),
    path('res_updatePassword', views.res_updatePassword, name='res_updatePassword'),
    # path('res_addDiscount', views.res_addDiscount, name='res_addDiscount'),
    path('res_editDiscount/<int:id>', views.res_editDiscount, name='res_editDiscount'),
    path('res_updateDiscount/<int:id>', views.res_updateDiscount, name='res_updateDiscount'),
    path('res_viewDiscount', views.res_viewDiscount, name='res_viewDiscount'),
    # path('res_deleteDiscount/<int:id>', views.res_deleteDiscount, name='res_deleteDiscount'),
    path('res_addAmbience', views.res_addAmbience, name='res_addAmbience'),
    path('res_viewAmbience', views.res_viewAmbience, name='res_viewAmbience'),
    path('res_deleteAmbience/<int:id>', views.res_deleteAmbience, name='res_deleteAmbience'),
    path('res_viewNewOrder', views.res_viewNewOrder, name='res_viewNewOrder'),
    path('res_viewAssignedAgent', views.res_viewAssignedAgent, name='res_viewAssignedAgent'),
    path('res_viewDeliveredOrder', views.res_viewDeliveredOrder, name='res_viewDeliveredOrder'),

]
