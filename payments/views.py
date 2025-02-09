import requests
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Transaction, Merchant
from .serializers import TransactionSerializer, MerchantSerializer

# Configure logging
logger = logging.getLogger(__name__)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        transaction_data = response.data
        
        # Notify external shopping app (Example API call)
        external_api_url = "http://127.0.0.1:8000/api/transactions/"
        
        try:
            external_response = requests.post(
                external_api_url, json=transaction_data, timeout=5
            )
            external_response.raise_for_status()  # Raise error for non-200 responses
            logger.info(f"External API notified successfully: {external_response.json()}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to notify external API: {str(e)}")
        
        return response


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
