from django.db import models
import logging
from django.utils.timezone import now

# Logger Setup
logger = logging.getLogger(__name__)


# Merchant Table
class Merchant(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


# Transaction Table
class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="transactions")
    product_name = models.CharField(max_length=255)
    time = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.status}"
