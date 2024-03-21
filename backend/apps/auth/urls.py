from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateView, LogoutView, RecoverPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateView.as_view(), name='auth_activate'),
    path('/recovery', RecoverPasswordView.as_view(), name='auth_recovery_password'),
    path('/logout', LogoutView.as_view(), name='auth_logout')
]
