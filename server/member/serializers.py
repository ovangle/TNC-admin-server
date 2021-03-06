from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from .basic.models import (
    Address, Contact, Income, Name, ResidentialStatus
)    
from .basic.serializers import (
    AddressSerializer, 
    ContactSerializer,
    EnergyAccountsSerializer,
    IncomeSerializer,
    NameSerializer,
    ResidentialStatusSerializer
)
from .basic.gender import Gender
from .models import Member

from .dependent.serializers import DependentSerializer
from .membership_term.serializers import MembershipTermSerializer

class MemberSerializer(serializers.Serializer):
    kind = serializers.CharField(read_only=True)

    id = serializers.IntegerField(read_only=True)

    name = NameSerializer()
    term = MembershipTermSerializer()

    gender = EnumField(enum_type=Gender)
    date_of_birth = serializers.DateField(allow_null=True)
    aboriginal_or_torres_strait_islander = serializers.NullBooleanField()
    register_consent = serializers.NullBooleanField()

    address = AddressSerializer()
    energy_accounts = EnergyAccountsSerializer()
    residential_status = ResidentialStatusSerializer()
    contact = ContactSerializer()
    income = IncomeSerializer()

    partner_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), 
        source='partner', 
        allow_null=True
    )

    dependents = DependentSerializer(many=True, source='carer.dependent_set')

    def validate_kind(self, data):
        kind = data.get('kind', None)
        if kind is None:
            raise serializers.ValidationError('No \'kind\' present in serialized data')
        if kind != Member.kind:
            raise serializers.ValidationError('Invalid \'kind\', expected {0}'.format(Member.kind))
        return data 

    def create(self, validated_data):
        name = self.fields['name'].create(validated_data.pop('name'), role=Member.objects.kind)
        term = self.fields['term'].create(validated_data.pop('term'))

        address = self.fields['address'].create(validated_data.pop('address'))
        residential_status = self.fields['residential_status'].create(validated_data.pop('residential_status'))
        contact = self.fields['contact'].create(validated_data.pop('contact'))
        income = self.fields['income'].create(validated_data.pop('income'))
        energy_accounts = self.fields['energy_accounts'].create(validated_data.pop('energy_accounts'))

        return Member.objects.create(
            name=name,
            term=term,
            gender=validated_data.pop('gender'),
            date_of_birth=validated_data.pop('date_of_birth'),
            aboriginal_or_torres_strait_islander=validated_data.pop('aboriginal_or_torres_strait_islander'),
            register_consent=validated_data.pop('register_consent'), 

            address=address,
            residential_status=residential_status,
            contact=contact,
            income=income,
            
            electricity_account=energy_accounts.get('ELECTRICITY', None),
            gas_account=energy_accounts.get('GAS', None),

            partner=validated_data.pop('partner')
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.aboriginal_or_torres_strait_islander = validated_data.get(
            'aboriginal_or_torres_strait_islander', 
            instance.aboriginal_or_torres_strait_islander
        )
        instance.register_consent = validated_data.get('register_consent', instance.register_consent)
        instance.address = validated_data.get('address', instance.address)
        instance.residential_status = validated_data.get('residential_status', instance.residential_status)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.income = validated_data.get('income', instance.income)
        instance.is_partnered = validated_data.get('is_partnered', instance.is_partnered)
        return instance

