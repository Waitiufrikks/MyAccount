from django.db import models

from users.models import User

class Account(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')  
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account(id={self.id}, user_id={self.user.id}, balance={self.balance})"