from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pesabank.models import Bank, Transaction
from .serializers import BankSerializer, TransactionSerializer

# This block defines three API views: BankListView, TransactionListView, and BankDetailView.

# BankListView handles GET and POST requests for retrieving all banks and creating a new bank.
# - GET request: Fetches all banks from the database and returns them in the response.
# - POST request: Accepts data to create a new bank and returns the created bank's data if valid.

# TransactionListView handles GET and POST requests for retrieving and creating transactions for a specific bank.
# - GET request: Fetches all transactions for the specified bank (based on bank_id) and returns them in the response.
# - POST request: Accepts transaction data, assigns it to the specified bank, and creates the transaction if the data is valid.

# BankDetailView handles GET requests for fetching details of a specific bank by its primary key (pk).
# - GET request: Retrieves a single bank by its ID, serializes it, and returns the data. If the bank is not found, it returns a 404 error response.



class BankListView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



class BankDetailView(APIView):
    def get(self, request, pk):
        try:
            bank = Bank.objects.get(pk=pk)  # Fetching the bank by its primary key
            serializer = BankSerializer(bank)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Bank.DoesNotExist:
            return Response({"error": "Bank not found"}, status=status.HTTP_404_NOT_FOUND)
