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
    path('res_changePassword', views.res_changePassword, name='res_changePassword'),
    path('res_updatePassword', views.res_updatePassword, name='res_updatePassword'),
    path('res_addDiscount', views.res_addDiscount, name='res_addDiscount'),
    path('res_viewDiscount', views.res_viewDiscount, name='res_viewDiscount'),
    path('res_deleteDiscount/<int:id>', views.res_deleteDiscount, name='res_deleteDiscount'),
]
