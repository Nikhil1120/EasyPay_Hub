from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login


def login_form(request):
    return render(request, "payments/login.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/api/')
        else:
            return render(request, "payments/login.html", context={'error':'Invalid username and password....!'})


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


# Payment Processing API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def initiate_payment(request):
    data = request.data
    try:
        merchant = Merchant.objects.create(
            name=data.get('merchant_name'),
            status='Active'
        )
        transaction = Transaction.objects.create(
            merchant=merchant,
            product_name=data.get('product_name'),
            product_cost=data.get('product_cost'),
            status='Pending'
        )
        logger.info(f'Payment initiated: Transaction ID {transaction.transaction_id}')
        return Response({
            'message': 'Payment initiated successfully',
            'transaction_id': transaction.transaction_id,
            'merchant_id': merchant.mid
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f'Error initiating payment: {str(e)}')
        return Response({'error': 'Failed to initiate payment'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    transaction_id = request.data.get('transaction_id')
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        transaction.status = 'Completed'
        transaction.save()
        logger.info(f'Payment verified: Transaction ID {transaction_id}')
        return Response({'message': 'Payment verified successfully'}, status=status.HTTP_200_OK)
    except Transaction.DoesNotExist:
        logger.warning(f'Invalid transaction ID: {transaction_id}')
        return Response({'error': 'Invalid transaction ID'}, status=status.HTTP_400_BAD_REQUEST)


# Webhook API for Real-time Updates
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment_webhook(request):
    data = request.data
    transaction_id = data.get('transaction_id')
    status_update = data.get('status')
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        transaction.status = status_update
        transaction.save()
        logger.info(f'Webhook received: Transaction {transaction_id} updated to {status_update}')
        return Response({'message': 'Webhook processed successfully'}, status=status.HTTP_200_OK)
    except Transaction.DoesNotExist:
        logger.warning(f'Webhook error: Invalid transaction ID {transaction_id}')
        return Response({'error': 'Invalid transaction ID'}, status=status.HTTP_400_BAD_REQUEST)
