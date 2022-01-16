from django.urls import path

from .views import AddAvatarView, UserListView, UserToAdminView

urlpatterns = [
    path('', UserListView.as_view()),
    path('/<int:pk>/admin', UserToAdminView.as_view()),
    path('/avatar', AddAvatarView.as_view())
]
