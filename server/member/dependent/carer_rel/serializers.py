from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from ...carer.serializers import CarerSerializer
from ...carer.models import Carer

from .living_arrangement import LivingArrangement
from .relation_type import RelationType

class CarerRelSerializer(serializers.Serializer):
    carer = CarerSerializer()
    living_arrangement = EnumField(enum_type=LivingArrangement)
    relation_type = EnumField(enum_type=RelationType)

    def to_representation(self, instance):
        print('CarerRel.to_representation')
        print('Instance: {0}'.format(instance))
        print('living arrangement')
        return super(CarerRelSerializer, self).to_representation(instance)