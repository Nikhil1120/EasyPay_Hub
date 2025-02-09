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
