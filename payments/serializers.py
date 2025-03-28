from rest_framework import serializers
from .models import *

class MerchantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchant
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = '__all__'
