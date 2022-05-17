from django.db import models
from authentication.models import User 
from store.models import Store 

# Create your models here.
class Booking(models.Model):


    name = models.CharField("username", max_length=255, default='')
    email = models.EmailField("Email Address", max_length=255, default='')
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE, default='SUPERMARKET')
    date = models.DateField(null=None, blank=False)
    booked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return str(self.store)



