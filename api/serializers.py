from rest_framework import serializers
from pesabank.models import Bank, Transaction


# This block defines two serializers: BankSerializer and TransactionSerializer.

# BankSerializer serializes the Bank model to convert its data into JSON format for the API.
# - It includes fields: id, name, and balance, which represent the basic information of a bank.

# TransactionSerializer serializes the Transaction model to convert its data into JSON format for the API.
# - It includes fields: id, bank (the related bank), date, and amount, which represent transaction details for a bank.

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'bank', 'date', 'amount']
