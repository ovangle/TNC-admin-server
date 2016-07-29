from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from ..carer.serializers import CarerSerializer
from ..carer.models import Carer

from .living_arrangement import LivingArrangement
from .relation_type import RelationType
from .models import CarerRel

class CarerRelSerializer(serializers.Serializer):
    carer = CarerSerializer()
    living_arrangement = EnumField(enum_type=LivingArrangement)
    relation_type = EnumField(enum_type=RelationType)

    def create(self, validated_data, dependent=None):
        if dependent is None:
            raise ValueError('Expected a valid dependent')

        carer_data = validated_data.get('carer')
        carer = self.fields['carer'].get(carer_data)

        if carer is None:
            return None
        import pdb; pdb.set_trace()
        return CarerRel.objects.create(
            carer=carer,
            living_arrangement=validated_data.pop('living_arrangement'),
            relation_type=validated_data.pop('relation_type'),
            dependent_id=dependent.id

        )