from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import generics
from rest_framework import permissions
from .models import MenuItem
from .serializers import MeniItemSerializer
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MeniItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MeniItemSerializer
