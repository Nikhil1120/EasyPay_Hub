from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'merchants', MerchantViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('api/initiate-payment/', initiate_payment, name='initiate_payment'),
    path('api/verify-payment/', verify_payment, name='verify_payment'),
    path('api/payment-webhook/', payment_webhook, name='payment_webhook'),
]
