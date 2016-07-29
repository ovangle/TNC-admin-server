from rest_framework import serializers

from ...basic.serializers import NameSerializer
from ...models import Member

from .models import Carer

class CarerSerializer(serializers.Serializer):
    name = NameSerializer(read_only=True)
    id = serializers.IntegerField(source='member_carer.id')

    def get(self, validated_data):
        id = validated_data.get('member_carer')['id']
        if id is None:
            return None
        return Carer.objects.get(member_carer__pk=id)
