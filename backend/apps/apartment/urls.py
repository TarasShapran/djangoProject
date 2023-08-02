from django.urls import path

from backend.apps.apartment.views import ApartmentRetrieveUpdateDestroyView, ApartmentsCreateView, ApartmentsListView

urlpatterns = [
    path('', ApartmentsCreateView.as_view()),
    path('/my', ApartmentsListView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view())
]
