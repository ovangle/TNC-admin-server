from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from .carer_rel.serializers import CarerRelSerializer
from .models import Dependent

from ..basic.gender import Gender
from ..basic.serializers import NameSerializer

class DependentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    carer_rels = CarerRelSerializer(many=True, source='carerrel_set')
    name = NameSerializer()
    gender = EnumField(enum_type=Gender)

    date_of_birth = serializers.DateField(allow_null=True)

    def create(self, validated_data, defer_save=False):
        """
        Create the dependent
        """
        name = self.fields['name'].create(validated_data.pop('name'), role=Dependent.kind)
        dependent = Dependent.objects.create(
            name=name, 
            gender=validated_data.pop('gender'),
            date_of_birth=validated_data.pop('date_of_birth')
        )

        import pdb; pdb.set_trace()
        carer_rel_datas = validated_data.pop('carerrel_set')
        for carer_rel_data in carer_rel_datas:
            serializer = CarerRelSerializer(carer_rel_data)
            carer_rel = serializer.create(carer_rel_data, dependent=dependent)
        return dependent 
