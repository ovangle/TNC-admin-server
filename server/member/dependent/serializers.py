from rest_framework import serializers

from .carer_rel.serializers import CarerRelSerializer

from ..basic.serializers import NameSerializer

class DependentSerializer(serializers.Serializer):
    carers = CarerRelSerializer(many=True, source='carerrel_set')
    name = NameSerializer()

    date_of_birth = serializers.DateField()

