from rest_framework import serializers
from .models import Bank, Transaction


"""
class BankSerializer- Serializes and deserializes Bank model data inheriting from the serializers.ModelSerializers
Converts the Bank model instances into JSON format for essential API communication.

Specifies the model to serialize
model = Bank

Specifies the fields to include in the serialized data
fields = ['id', 'name', 'balance'] 

"""

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ['id', 'name', 'balance'] 


"""
class TransactionSerializers- Serializes and deserializes Transaction model data.
Converts the Transaction model instances into JSON format for essential API communication.
"""
class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id', 'bank', 'amount', 'transaction_type', 'date']  
