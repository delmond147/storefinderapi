from rest_framework import serializers
from .models import Booking 

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking 
        fields = ['store', 'payment_type', 'booked_on']
