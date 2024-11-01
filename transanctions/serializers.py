from rest_framework import serializers
from accounts.models import Account
from .models import Transaction 

class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())  
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    type = serializers.ChoiceField(choices=Transaction.TRANSACTION_TYPE_CHOICES, required=True)
    date = serializers.DateTimeField(read_only=True)  
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser maior que zero.")
        return value
    def create(self, validated_data):
        transaction = Transaction(**validated_data) 
        transaction.save() 
        return transaction

    def update(self, instance: Transaction, validated_data: dict) -> Transaction:
        # Atualiza os campos da instância de Transaction
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save() 
        return instance