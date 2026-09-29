from rest_framework import serializers
from pairing.models import PairingToken

class PairingTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairingToken
        fields = ('id', 'token', 'expires_at', 'used', 'created_at')
