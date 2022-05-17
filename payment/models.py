from django.db import models
from booking.models import Booking
# Create your models here

class Payment(models.Model):
    
    item = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=True)
    paid_on = models.DateTimeField(auto_now_add=False, auto_now=True)
   

    def __str__(self):
        return str(self.item)
