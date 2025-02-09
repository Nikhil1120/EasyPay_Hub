from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import TransactionViewSet, MerchantViewSet

# Create a router
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)  # /api/transactions/
router.register(r'merchants', MerchantViewSet)  # /api/merchants/

urlpatterns = [
    path('api/', include(router.urls)),
]
