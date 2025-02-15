from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import *

router = DefaultRouter()
router.register(r'merchants', MerchantViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-transaction-status/<int:transaction_id>/', TransactionStatusAPI.as_view(), name='transaction_status'),
]
