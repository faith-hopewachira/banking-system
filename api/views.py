from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, Transaction
from .serializers import BankSerializer, TransactionSerializer
from django.contrib.auth.models import User


"""
class BankListView- API endpoint to handle requests related to banks for a user.
- GET: Returns all banks belonging to the authenticated user, along with their total balance.

FIELDS
user = Get the currently authenticated user
banks = Retrieve all banks owned by the user
Serialize the data, then calculate the total balance across all the user's banks (e.g Equity, ABSA and NCBA)
"""

class BankListView(APIView):

    def get(self, request):
        user = request.user
        banks = Bank.objects.filter(user=user)
        serializer = BankSerializer(banks, many=True)
        total_balance = sum([bank.balance for bank in banks])
        return Response({"banks": serializer.data, "total_balance": total_balance}, status=status.HTTP_200_OK)


"""
class TransactionListView- API endpoint to handle requests related to transactions for a specific bank.
- GET: Returns all transactions for the specified bank.
- POST: Adds a new transaction to the specified bank.

GET METHOD
transactions = Retrieve transactions for the bank
serializer = Serialize the data


POST METHOD
data - Get the request data
data['bank']- Deserialize the data and then validate the data then save the validated data
"""
class TransactionListView(APIView):

    def get(self, request, bank_id):
        transactions = Transaction.objects.filter(bank_id=bank_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, bank_id):
        data = request.data
        data['bank'] = bank_id
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
