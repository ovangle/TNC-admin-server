from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from member.basic.serializers import (
    AddressSerializer, 
    ContactSerializer,
    NameSerializer 
)
from user.models import User

from .staff_type import StaffType
from .availability.serializers import AvailabilitySerializer
from .induction_survey.serializers import StaffInductionSurveySerializer
from .models import StaffMember

class StaffMemberSerializer(serializers.Serializer):
    kind = serializers.CharField(max_length=32)
    id = serializers.IntegerField()
    type = EnumField(enum_type=StaffType)

    user_id = serializers.IntegerField()

    name = NameSerializer(required=True)
    availability = AvailabilitySerializer(required=False)

    address = AddressSerializer(required=True)
    contact = ContactSerializer(required=True)

    date_of_birth = serializers.DateField()

    # TODO: Remove this
    induction_survey = StaffInductionSurveySerializer()

    def validate_user_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError('No user with id \'{0}\''.format(user_id))

    def create(self, validated_data):
        return StaffMember.objects.create(
            user=validated_data.pop('user_id'),
            name=self.fields['name'].create(validated_data.pop('name')),
            address=self.fields['address'].create(validated_data.pop('address')),
            contact=self.fields['contact'].create(validated_data.pop('contact')),
            availability=StaffMemberSerializer.availability.create(validated_data.pop('availability',dict())),
            date_of_birth=validated_data.pop('date_of_birth') 
        )

