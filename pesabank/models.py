from django.db import models
from django.contrib.auth.models import User


"""
class Bank-Represents a bank associated with a user.
Each bank has a name, a user (owner), and a balance.

name= The name of the bank the user is registered with
user = The user who owns this bank. If the user is deleted, all their banks are deleted too.
balance = The total balance in the bank account.

"""
class Bank(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='banks')  
    balance = models.DecimalField(max_digits=12, decimal_places=2)  

    def __str__(self):
        """
        Returns a string representation of the Bank model.
        """
        return f"{self.name} - {self.user.username}"



"""
class Transaction- Represents a transaction in a specific bank account.
Each transaction has an amount, type, and date.

FIELDS OF TRANSACTION
bank- represents the name of the bank
amount- the total amount in the bank (positive or negative depending on the amount)
transaction_type- the type of transaction.
DEPOSIT- adding money to the account
WITHDRAWAL- removing money from the account
EXPENSE- represents money spent on something
date- the date the transaction occurred
"""
class Transaction(models.Model):

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='transactions')  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('EXPENSE', 'Expense'),
    ]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)  
    date = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the Transaction model.
        """
        return f"{self.transaction_type} - {self.amount} ({self.bank.name})"
