from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        fields = (
            "name",
            "avatar",
            "username",
        )
        
        
