# EasyPay_Hub
## Problem Statement
In modern e-commerce, multiple shopping applications require seamless and secure payment processing. However, integrating multiple payment gateways directly into each shopping app can be complex, time-consuming, and expensive. Additionally, merchants need a streamlined way to track transactions and manage their sales efficiently.

## Solution: EasyPay HUB
**EasyPay HUB** is a third-party payment gateway that acts as a bridge between shopping apps and payment processing. It simplifies the payment process by allowing merchants to register and process transactions securely through a centralized system. The platform maintains two core tables:
- **Merchant Table**: Stores merchant details and records the purchases made.
- **Transaction Table**: Keeps track of transaction details, including product name, timestamp, status, and cost.

## Problems Overcome by EasyPay HUB
1. **Simplified Payment Integration**: Shopping apps no longer need to build individual payment solutions; they can integrate EasyPay HUB for seamless transactions.
2. **Centralized Transaction Management**: Merchants can track their transactions in one place, reducing complexity.
3. **Improved Security & Reliability**: Transactions are stored in a structured database with status tracking to prevent fraud or errors.
4. **Real-time Transaction Updates**: The system records transaction statuses and amounts in real-time, ensuring transparency.
5. **Scalability**: EasyPay HUB can be used by multiple merchants without affecting performance, making it a scalable solution.

## Advantages of EasyPay HUB
✔ **Efficient Payment Processing** – Automates transaction recording and merchant payments.
✔ **Cost-Effective** – Reduces the need for shopping apps to develop custom payment gateways.
✔ **Easy Integration** – RESTful API ensures seamless integration with various shopping apps.
✔ **Secure & Reliable** – Reduces transaction failures and provides clear transaction history.
✔ **Merchant-Friendly** – Allows merchants to focus on business growth instead of payment complexities.

---

## Code Implementation

### **1. Install Dependencies**
```sh
pip install django djangorestframework mysqlclient requests
```

### **2. Create Django Project & App**
```sh
django-admin startproject easypayhub
cd easypayhub
django-admin startapp payments
```

### **3. Configure MySQL Database** (settings.py)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'easypayhub_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### **4. Models (models.py)**
```python
import uuid
from django.db import models
from django.utils.timezone import now

class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
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
```

### **5. Serializers (serializers.py)**
```python
from rest_framework import serializers
from .models import Transaction, Merchant

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
```

### **6. Views with REST API Communication (views.py)**
```python
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Transaction, Merchant
from .serializers import TransactionSerializer, MerchantSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        transaction_data = response.data
        
        # Notify external shopping app (Example API call)
        external_api_url = "https://shoppingapp.com/api/notify_transaction"
        requests.post(external_api_url, json=transaction_data)
        
        return response

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
```

### **7. URLs (urls.py)**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, MerchantViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'merchants', MerchantViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### **8. Register App in Django (settings.py)**
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'payments',
]
```

### **9. Migrate Database**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **10. Run Development Server**
```sh
python manage.py runserver
```

## Future Improvements
1. **Security Enhancements** – Implement JWT authentication and encryption for sensitive data.
2. **Webhook Integration** – Notify merchants in real time about transaction status.
3. **Multi-Currency Support** – Enable payments in different currencies.
4. **Fraud Detection System** – Use AI/ML to detect fraudulent transactions.
5. **Admin Dashboard** – Provide analytics and transaction insights.
6. **Payment Gateway Support** – Integrate third-party gateways like Stripe, Razorpay, and PayPal.
7. **Subscription & EMI Payments** – Allow installment-based payments for merchants.

Now, the **EasyPay HUB** API can communicate with shopping applications via REST API, notifying them about transaction updates
