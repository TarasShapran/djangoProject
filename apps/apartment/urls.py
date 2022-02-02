from django.urls import path

from apps.apartment.views import ApartmentRetrieveUpdateDestroyView, ApartmentsListCreateView

urlpatterns = [
    path('', ApartmentsListCreateView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view())
]
