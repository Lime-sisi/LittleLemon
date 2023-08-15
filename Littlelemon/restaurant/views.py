from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import permissions
from .models import menu, booking
from. serializers import MenuSeriazlizer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSeriazlizer

class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSeriazlizer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


