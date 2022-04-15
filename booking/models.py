from django.db import models
from authentication.models import User 
from store.models import Store 

# Create your models here.
class Booking(models.Model):

    PAYMENT_TYPE = [
        ('MOBILE MONEY', [
            ('MTN', 'MTN'),
            ('ORANGE', 'Orange'),
        ]),
        ('BANK TRANSACTION', [
            ('MASTER', 'Debit Card'),
            ('MASTER', 'Credit Card'),
            ('MASTER', 'Visa Card'),
        ]),
        ('CRYPTO CURRENCY', [
            ('BITCOIN', 'Bitcoin'),
            ('PLANTICOIN', 'Planticoin'),
        ]),
    ]

    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # category = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE, default='SUPERMARKET')
    payment_type = models.CharField(choices=PAYMENT_TYPE, default='MTN', max_length=255)
    # amount = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    date = models.DateField(null=None, blank=False)
    booked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return str(self.store)



