from rest_framework.views import APIView, status, Request, Response
from accounts.models import Account
from .models import Transaction  
from accounts.serializers import AccountSerializer
from .serializers import TransactionSerializer  

class TransactionView(APIView):
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
    def get(self, request, transaction_id) -> Response:
        try:
            transaction = Transaction.objects.get(id=transaction_id)  
        except Transaction.DoesNotExist:
            return Response({"message": "Transação não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction) 
        return Response(serializer.data, status=status.HTTP_200_OK)  
