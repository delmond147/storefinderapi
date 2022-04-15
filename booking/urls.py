from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingListAPIView.as_view(), name='booking'),
    path('<int:id>', views.BookingDetialsAPIView.as_view(), name='booking'),
]