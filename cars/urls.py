from django.urls import path

from cars.views import CarsListCreateView, CarsRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarsListCreateView.as_view()),
    path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view())
]
