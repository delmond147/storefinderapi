from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookingSerializer
from .models import Booking
from rest_framework import permissions
from .permissions import IsOwner

# Create your views here.

class BookingListAPIView(ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    query = Booking.objects.all()

    def create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.query.filter(owner=self.request.user)


class BookingDetialsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    query = Booking.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.query.filter(owner=self.request.user)
