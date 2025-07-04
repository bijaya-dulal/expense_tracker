from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, UserSerializer

# Create your views here.

#permissions
class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
