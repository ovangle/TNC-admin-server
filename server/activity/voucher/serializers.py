from decimal import Decimal
from rest_framework import serializers

from member.basic.energy_account.account_type import EnergyAccountType

from .models import FoodcareVoucher, ChemistVoucher, EAPAVoucher
from .eapa_voucher_book import (
    EAPAVoucherBook, 
    EAPAVoucherBookSerializer,
    validate_voucher_books
)    

from ext.rest_framework.serializers import GenericSerializer
from member.basic.serializers import EnergyAccountBillsSerializer


class VoucherSerializer(GenericSerializer):

    @property
    def subkinds(self):
        return {
            FoodcareVoucher.objects.kind: FoodcareVoucherSerializer, 
            ChemistVoucher.objects.kind: ChemistVoucherSerializer,
            EAPAVoucher.objects.kind: EAPAVoucherSerializer
        }

class FoodcareVoucherSerializer(VoucherSerializer):
    pass

class ChemistVoucherSerializer(VoucherSerializer):
    pass

class EAPAVoucherSerializer(VoucherSerializer):
    bills = EnergyAccountBillsSerializer()

    is_denying_basic_needs = serializers.BooleanField()
    is_facing_disconnection = serializers.BooleanField()
    is_disconnected = serializers.BooleanField()

    is_granted_limit_exemption = serializers.BooleanField()
    limit_exemption_description = serializers.CharField(allow_blank=True)

    is_customer_declaration_signed = serializers.BooleanField()
    is_assessor_declaration_signed = serializers.BooleanField()

    voucher_books = serializers.ListField(
        child=EAPAVoucherBookSerializer()
    )

    def validate(self, data):
        is_granted_limit_exemption = data['is_granted_limit_exemption']

        self._validate_limit_exemption_description(
            is_gratned_limit_exemption, 
            data['limit_exemption_description']
        )

        value = self.get_assessed_value(data['bills'], is_granted_limit_exemption)        
        self._validate_voucher_books(data['voucher_books'], value)

    def get_assessed_value(self, bill_datas, is_granted_limit_exemption=False):
        total_bill_value = sum(
            bill.get('value', 0) for bill in bill_datas.values()
        )
        # EAPA voucher bills are quantized in $50 units
        total_bill_value = 50 * (total_bill_value // 50)

        if is_granted_limit_exemption:
            return min(total_bill_value, Decimal('250'))
        else:
            return total_bill_value


    def _validate_voucher_books(self, voucher_books, assessed_value):
        # The number of issued vouchers
        expect_count = int(assessed_value // 50)
        validate_voucher_books(voucher_books, expect_count=expect_count)

    def _validate_limit_exemption_description(self, is_granted_limit_exemption, limit_exemption_description):
        if is_granted_limit_exemption:
            if limit_exemption_description == '':
                raise serializers.ValidationError(
                    'A description is required when granting an exemption to EAPA limits'
                )



    def validate_bills(self, bill_datas):
        has_electricity = bill_datas.get('ELECTRICITY') is not None
        has_gas = bill_datas.get('GAS') is not None

        if not (has_electricity or has_gas):
            raise serializers.ValidationError(
                'An ELECTRICITY or GAS bill must be present on the voucher'
            )
        return bill_datas


    def create(self, validated_data):
        task = validated_data.get('task')
        if task is None:
            raise ValueError('The member that this voucher applies to must be provided')

        bill_serializer = EnergyAccountBillsSerializer(data=validated_data.get('bills'))
        bill_serializer.is_valid()

        import pdb; pdb.set_trace()

        bills = bill_serializer.save(member=task.member)

        import pdb; pdb.set_trace();

        voucher = EAPAVoucher(
            task=task,
            gas_bill=bills.get('ELECTRICITY'),
            electricity_bill=bills.get('GAS'),
            is_denying_basic_needs=validated_data['is_denying_basic_needs'],
            is_facing_disconnection=validated_data['is_facing_disconnection'],
            is_disconnected=validated_data['is_disconnected'],
            is_granted_limit_exemption=validated_data['is_granted_limit_exemption'],
            limit_exemption_description=validated_data['limit_exemption_description'],
            is_customer_declaration_signed=validated_data['is_customer_declaration_signed'],
            is_assessor_declaration_signed=validated_data['is_assessor_declaration_signed']
        )
        voucher.save()
        return voucher

