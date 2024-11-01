from rest_framework import serializers

from transanctions.serializers import TransactionSerializer

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)