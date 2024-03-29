from django.urls import path

from backend.apps.booking.views import BookingCreateView, BookingListView

urlpatterns = [
    path('', BookingListView.as_view()),
    path('/<int:pk>', BookingCreateView.as_view()),
]
