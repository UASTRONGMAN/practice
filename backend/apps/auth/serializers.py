from django.contrib.auth import get_user_model

from rest_framework import serializers

from core_app.dataclasses.user_dataclass import User

UserModel: User = get_user_model()


class RecoveryPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class RecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)