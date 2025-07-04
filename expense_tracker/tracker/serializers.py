from rest_framework import serializers
from .models import ExpenseIncome
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at', 'total']

    def get_total(self, obj):
        return obj.total

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
