from django.urls import path

from autopark.views import AutoParkListCreateView, AutoParkAddCarView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view()),
]
