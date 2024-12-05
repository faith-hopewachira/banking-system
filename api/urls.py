
from django.urls import path
from .views import BankDetailView, BankListView, TransactionListView

urlpatterns = [
    path('api/banks/', BankListView.as_view(), name='bank-list'),  # GET and POST banks
    path('api/banks/<int:bank_id>/transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),

]

