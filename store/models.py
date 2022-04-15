
from django.db import models
from authentication.models import User
from location_field.models.plain import PlainLocationField

# Create your models here.


class Store(models.Model):

    SOURCE_OPTIONS = [
        ('SUPERMARKET', 'SUPERMARKET'),
        ('GROCER_STORE', 'GROCER STORE'),
        ('BUTCHER', 'BUTCHER'),
        ('BAKER', 'BAKER'),
        ('FISHMONGER', 'FISH MONGER'),
        ('CHEMIST', 'CHEMIST or PHAMARCY'),
        ('FASHION', 'FASHION'),
        ('BOOK_SHOP', 'BOOK SHOP'),
        ('HAIRDRESSER|BARBER', 'HAIRDRESSER & BARBER'),
        # ('FLOWER_SHOP', 'FLOWER_SHOP'),
        ('PATROL_STATION', 'PATROL STATION'),
        ('OTHERS', 'OTHERS')
    ]

    STATUS = [
        ('AVAILABLE', 'Available'),
        ('BOOKED', 'Not Available'),
    ]


    category = models.CharField(choices=SOURCE_OPTIONS, max_length=255, default='FASHION')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=255)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    image = models.ImageField(upload_to='images', height_field=None, width_field=None)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

