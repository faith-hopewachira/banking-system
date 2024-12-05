from .views import BankListView, TransactionListView
from django.urls import path

urlpatterns = [
    # Below is an endpoint to list all banks for the authenticated user
    path('banks/', BankListView.as_view(), name='bank-list'),  
    # Below is an endpoint to GET and POST transactions for a specific bank
    path('banks/<int:bank_id>/transactions/', TransactionListView.as_view(), name='transaction-list'),  
]
