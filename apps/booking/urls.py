from django.urls import path

from apps.booking.views import BookingListCreateView

urlpatterns = [
    path('/<int:pk>', BookingListCreateView.as_view()),
]
