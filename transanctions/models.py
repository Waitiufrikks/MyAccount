from django.db import models

from accounts.models import Account  

class Transaction(models.Model):  
    DEPOSIT = 'deposito'  
    WITHDRAWAL = 'saque'  
    
    TRANSACTION_TYPE_CHOICES = [  
        (DEPOSIT, 'Depósito'),  
        (WITHDRAWAL, 'Saque'),  
    ]  

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    type = models.CharField(max_length=8, choices=TRANSACTION_TYPE_CHOICES) 
    date = models.DateTimeField(auto_now_add=True,)  