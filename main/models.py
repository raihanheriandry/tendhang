import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey Bola'),
        ('shoes', 'Sepatu Bola'),
        ('ball', 'Bola'),
        ('accessories', 'Aksesoris'),
        ('training', 'Alat Latihan'),
        ('jacket', 'Jaket'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.IntegerField()
    description = models.TextField()  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True) 
    is_featured = models.BooleanField(default=False) 
    stock = models.IntegerField(default=0)   
    sold = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=50, blank=True, null=True) 
    
    def __str__(self):
        return self.name
    
    @property
    def is_best(self):
        return self.sold > 20
        
    def decrease_stock(self, quantity=1):
        if self.stock < quantity:
            print(f"Not enough stock for {self.name}!")
        else:
            self.stock -= quantity
            self.sold += quantity
            self.save()