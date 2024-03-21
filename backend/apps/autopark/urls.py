from django.urls import path

from backend.apps.autopark.views import AutoParkAddCarView, AutoParkListCreateView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view()),
]
