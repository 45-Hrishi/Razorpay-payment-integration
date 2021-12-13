from django.db import models

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=150)
    amount = models.CharField(max_length=6)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_id}|{self.paid}" 