from django.db import models


# This block defines two models: Bank and Transaction.
# The Bank model represents a financial institution with the following attributes:
# - 'name': A CharField that stores the name of the bank (maximum length of 255 characters).
# - 'balance': A DecimalField that stores the current balance of the bank, allowing for up to 10 digits with 2 decimal places.
# The Bank model also includes a __str__ method to return the bank's name when the object is printed or displayed.

# The Transaction model represents a financial transaction associated with a specific bank.
# It includes the following fields:
# - 'bank': A ForeignKey to the Bank model, establishing a many-to-one relationship. Each transaction is linked to a bank, and when a bank is deleted, all its associated transactions are also deleted (on_delete=models.CASCADE).
# - 'date': A DateField that stores the date the transaction occurred.
# - 'amount': A DecimalField that stores the transaction amount, allowing up to 10 digits with 2 decimal places.
# The Transaction model also includes a __str__ method that returns a string representation of the transaction, 
# formatted as the amount, the associated bank's name, and the transaction date.

class Bank(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    bank = models.ForeignKey(Bank, related_name="transactions", on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount} - {self.bank.name} on {self.date}"
