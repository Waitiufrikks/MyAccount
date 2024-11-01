from rest_framework import permissions
from accounts.models import Account

class TransactionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.method == "POST":
            transaction_type = request.data.get("type")
            account_id = request.data.get("account")

            # Verifica se a transação é um saque e se o usuário é o dono da conta
            if transaction_type == 'saque':
                try:
                    account = Account.objects.get(id=account_id)
                except Account.DoesNotExist:
                    return False
                return account.user == request.user  
            
            # Permite depósitos a qualquer usuário autenticado
            elif transaction_type == 'deposito':
                return True

        return request.method in permissions.SAFE_METHODS