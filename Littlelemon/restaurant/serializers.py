from rest_framework import serializers
from django.contrib.auth.models import User
from.models import menu, booking

class MenuSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = "__all__"

