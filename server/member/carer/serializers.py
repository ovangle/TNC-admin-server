from rest_framework import serializers

from ..basic.serializers import NameSerializer

from .models import Carer

class CarerSerializer(serializers.Serializer):
    kind = serializers.CharField(max_length=32, read_only=True)
    id = serializers.IntegerField(source='pk', read_only=True)

    name = NameSerializer(read_only=True)

    def validate_kind(self, data):
        if not data['kind'] == Carer.kind:
            raise serializers.ValidationError('Invalid kind for Carer: {0}'.format(data['kind']))
            

