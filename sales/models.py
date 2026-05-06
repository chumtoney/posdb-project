from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=100, default='General') 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('open',      'Open'),
        ('paid',      'Paid'),
        ('refunded',  'Refunded'),
        ('cancelled', 'Cancelled'),
    ]

    cashier    = models.ForeignKey(
                     User,
                     on_delete=models.SET_NULL,
                     null=True,
                     related_name='orders',
                  )
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    notes      = models.TextField(blank=True)

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        name = self.cashier.username if self.cashier else 'unknown'
        return f"Order #{self.pk}  [{self.status.upper()}]  by {name} — ${self.total:.2f}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # <--- ត្រូវប្រាកដថាឈ្មោះនេះជា 'quantity'
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
