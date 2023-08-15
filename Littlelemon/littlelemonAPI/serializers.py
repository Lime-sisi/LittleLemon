from rest_framework.serializers import ModelSerializer
from .models import MenuItem

class MeniItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
