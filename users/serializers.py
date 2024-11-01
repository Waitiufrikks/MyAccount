from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=40, required=True)  # Alterado para "username"
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):  
        email = data.get("email")  
        username = data.get("username")  
        user_id = self.instance.id if self.instance else None  

        if User.objects.filter(email=email).exclude(id=user_id).exists():  
            raise serializers.ValidationError({"email": ["email already registered."]})  
        
        if User.objects.filter(username=username).exclude(id=user_id).exists():  
            raise serializers.ValidationError({"username": ["username already registered."]})  

        return data  
    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  # Assegure-se de hashear a senha  
        user.save()  
        return user  
    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)
        for key, value in validated_data.items():
            if key != 'password':
                setattr(instance, key, value)

        instance.save()

        return instance  
