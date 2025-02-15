from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# API to display transaction status
class TransactionStatusAPI(APIView):
    
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
            if transaction.status == "Completed":
                return Response({
                    "message": "Your order is successful.",
                    "transaction_id": transaction.transaction_id,
                    "product_name": transaction.product_name,
                    "product_cost": transaction.product_cost
                }, status=status.HTTP_200_OK)
            elif transaction.status == "Pending":
                return Response({"message": "Your order is pending."}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    "message": "Your order has failed.",
                    "transaction_id": transaction.transaction_id,
                    "product_name": transaction.product_name,
                    "product_cost": transaction.product_cost
                }, status=status.HTTP_400_BAD_REQUEST)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)
