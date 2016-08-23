from rest_framework import serializers

from ext.rest_framework.fields import EnumField

from ..name.serializers import NameSerializer
from ..address.serializers import AddressSerializer

from .energy_retailer import EnergyRetailer
from .account_type import EnergyAccountType
from .models import EnergyAccount, EnergyAccountBill


class EnergyAccountSerializer(serializers.Serializer):
    type = EnumField(enum_type=EnergyAccountType)
    retailer = EnumField(enum_type=EnergyRetailer, allow_null=True)
    account_number = serializers.CharField(max_length=32, allow_blank=True)

    def create(self, validated_data, member=None):
        if member is None:
            raise ValueError('member must be provided')

        account = EnergyAccount(
            type=validated_data['type'],
            retailer=validated_data.get('retailer'),
            account_number=validated_data.get('account_number'),
        )    
        account.save()
        if account.type is EnergyAccountType.electricity:
            member.electricity_account = account
        elif account.type is EnergyAccountType.gas:
            member.gas_account = account
        member.save()
        return account


class EnergyAccountsSerializer(serializers.Serializer):
    # These field names are CAPS because the entries in the accounts dict are enum values
    GAS = EnergyAccountSerializer(allow_null=True)
    ELECTRICITY = EnergyAccountSerializer(allow_null=True)

    def create(self, validated_data):
        created = {}

        gas_account = validated_data.pop('GAS', None)
        if gas_account_data is not None:
            created['GAS'] = self.fields['GAS'].create(gas_account)

        electricity_account_data = validated_data.pop('ELECTRICITY', None)
        if electricity_account is not None:
            created['ELECTRICITY'] = self.fields['ELECTRICITY'].create(electricity_account_data)

        return created

class EnergyAccountBillSerializer(serializers.Serializer):
    account = EnergyAccountSerializer()
    value = serializers.DecimalField(9,2)

    def create(self, validated_data, member=None):
        account = self.fields['account'].create(validated_data.pop('account'), member=member)
        return EnergyAccountBill.objects.create(
            account=account, 
            value=validated_data.pop('value')
        )

class EnergyAccountBillsSerializer(serializers.Serializer):

    # These field names are CAPS because the entries in the bills dict are enum values 
    GAS = EnergyAccountBillSerializer(allow_null=True, required=False)
    ELECTRICITY = EnergyAccountBillSerializer(allow_null=True, required=False)

    def create(self, validated_data):
        member = validated_data.get('member')
        if member is None:
            raise ValueError('Member must be provided')
        created = {}

        gas_bill = validated_data.pop('GAS', None)
        if gas_bill is not None:
            created['GAS'] = self.fields['GAS'].create(gas_bill, member=member)

        electricity_bill = validated_data.pop('ELECTRICITY', None)
        if electricity_bill is not None:
            created['ELECTRICITY'] = self.fields['ELECTRICITY'].create(electricity_bill, member=member)

        return created


