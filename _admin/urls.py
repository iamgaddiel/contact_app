from django.urls import path

from .views import (
    ListUsers,
    UserDetailView,
    UserDeleteView,
    UserUpdateView
)

urlpatterns = [
    path('user_list/', ListUsers.as_view(), name='admin_user_list'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='admin_user_detail'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name='admin_user_delete'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='admin_user_update'),
]
