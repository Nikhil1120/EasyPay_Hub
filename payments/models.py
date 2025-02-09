from django.db import models
from django.utils.timezone import now


class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=255)
    time = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.status}"


class Merchant(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
