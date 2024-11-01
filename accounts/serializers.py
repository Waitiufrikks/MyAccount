from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True) 