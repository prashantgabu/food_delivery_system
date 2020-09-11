from django.urls import path
from . import views
urlpatterns = [
    path('', views.agent_login, name='agent_login'),
    path('agent_register', views.agent_register, name='agent_register'),
    path('agent_dashboard', views.agent_dashboard, name='agent_dashboard'),
    path('agent_editProfile', views.agent_editProfile, name='agent_editProfile'),
    path('agent_updateProfile', views.agent_updateProfile, name='agent_updateProfile'),
    path('agent_changePassword', views.agent_changePassword, name='agent_changePassword'),
    path('agent_updatePassword', views.agent_updatePassword, name='agent_updatePassword'),
    path('agent_verification', views.agent_verification, name='agent_verification'),
    path('agent_viewNewOrder', views.agent_viewNewOrder, name='agent_viewNewOrder'),
    path('agent_acceptOrder/<int:id>', views.agent_acceptOrder, name='agent_acceptOrder'),
    path('agent_viewAcceptedOrder', views.agent_viewAcceptedOrder, name='agent_viewAcceptedOrder'),
    path('agent_viewOrderHistory', views.agent_viewOrderHistory, name='agent_viewOrderHistory'),
]