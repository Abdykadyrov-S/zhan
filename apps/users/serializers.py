from rest_framework import serializers

from apps.users.models import User
from apps.products.serializers import ProductsSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'promo_code')
        
class UserDetailSerializer(serializers.ModelSerializer):
    user_products = ProductsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'phone', 'promo_code', 'user_products')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only=True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'phone', 'promo_code', 'password', 'password2')

    def validate(self, attrs):
        if len(attrs['phone']) == 13:
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Пароли отличаются"})
            elif '+996' not in attrs['phone']:
                raise serializers.ValidationError({"phone": "Напишите номер с +996"})
        else:
            raise serializers.ValidationError({"phone": " Длина номера должен быть равен 12"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=self.initial_data.get("email"),
            image=validated_data['image'],
            phone=self.initial_data.get("phone"),
            promo_code=self.initial_data.get("promo_code"),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
