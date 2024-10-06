from django.urls import path

from apps.users.views import (
    BanUserView,
    CancelAdminUserView,
    CreateAdminUserView,
    UnbanUserView,
    UserMeView,
    UsersListCreateView,
)

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/me', UserMeView.as_view(), name='user_me'),
    path('/<int:pk>/ban', BanUserView.as_view(), name='ban_user'),
    path('/<int:pk>/unban', UnbanUserView.as_view(), name='unban_user'),
    path('/<int:pk>/create_admin', CreateAdminUserView.as_view(), name='create_admin_user'),
    path('/<int:pk>/cancel_admin', CancelAdminUserView.as_view(), name='cancel_admin_user'),
]