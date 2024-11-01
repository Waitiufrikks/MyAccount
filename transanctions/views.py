from decimal import Decimal
from rest_framework.views import APIView, status, Request, Response
from accounts.models import Account
from transanctions.permissions import TransactionPermission
from .models import Transaction  
from accounts.serializers import AccountSerializer
from .serializers import TransactionSerializer  
from rest_framework_simplejwt.authentication import JWTAuthentication

class TransactionView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request) -> Response:
        transactions = Transaction.objects.all() 
        serializer = TransactionSerializer(transactions, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def post(self, request) -> Response:
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            transaction_type = serializer.validated_data.get('type') 
            amount = serializer.validated_data.get('amount')  
            account = serializer.validated_data.get('account')  
            
            # Lógica para atualizar o saldo da conta
            if transaction_type == 'saque':
                if account.balance < amount:
                    return Response({"message": "Saldo insuficiente."}, status=status.HTTP_400_BAD_REQUEST)  # Saldo insuficiente
                account.balance -= amount  # Diminui o saldo para saques
            elif transaction_type == 'deposito':
                account.balance += amount  # Aumenta o saldo para depósitos
            
            account.save()  
            transaction = serializer.save()  
            
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)  # Retorna os dados da nova transação criada
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, transaction_id) -> Response:
        try:
            transaction = Transaction.objects.get(id=transaction_id)
        except Transaction.DoesNotExist:
            return Response({"message": "Transação não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, transaction_id, target_account_id) -> Response:
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            target_account = Account.objects.get(id=target_account_id)
        except Transaction.DoesNotExist:
            return Response({"message": "Transação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Account.DoesNotExist:
            return Response({"message": "Conta alvo não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        amount = request.data.get('amount')

        if amount is None or Decimal(amount) <= 0:
            return Response({"message": "Por favor, forneça um valor válido para o depósito."}, status=status.HTTP_400_BAD_REQUEST)
        target_account.balance += Decimal(amount)
        target_account.save()

        # Cria uma nova transação de depósito para registro
        new_transaction_data = {
            "account": target_account.id,
            "amount": amount,
            "type": "deposito"
        }
        new_transaction_serializer = TransactionSerializer(data=new_transaction_data)

        if new_transaction_serializer.is_valid():
            new_transaction = new_transaction_serializer.save()
            return Response(TransactionSerializer(new_transaction).data, status=status.HTTP_201_CREATED)

        return Response(new_transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)