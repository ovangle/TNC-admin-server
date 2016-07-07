from rest_framework import serializers

class EAPAAssessmentSerializer(serializers.Serializer):
    is_no_relation_to_assessor = serializers.BooleanField()  
    bill_sighted = serializers.BooleanField()

    is_name_on_bill = serializers.BooleanField()
    is_address_on_bill = serializers.BooleanField() 

    is_residential_electicity_or_gas_account = serializers.BooleanField()

    is_experiencing_financial_hardship = serializers.BooleanField()
    is_denying_basic_needs = serializers.BooleanField()
    is_facing_disconnection = serializers.BooleanField() 

    has_contacted_retailer_to_check_payment_plans = serializers.BooleanField()
    has_contacted_retailer_to_check_energy_rebates = serializers.BooleanField()
    has_contacted_retailer_to_check_updated_balance = serializers.BooleanField()
    has_contacted_retailer_to_check_eapa_payments = serializers.BooleanField()

    is_receiving_over_limit_on_current_bill = serializers.BooleanField()
    is_receiving_over_limit_for_financial_year = serializers.BooleanField()
    is_receiving_assistance_more_than_twice = serializers.BooleanField()

    limit_exemption_description = serializers.CharField()

    signed_privacy_agreement = serializers.BooleanField()

    is_bill_stamped = serializers.BooleanField() 

    understood_voucher_processing = serializers.BooleanField()

    consent_to_retain_data = serializers.BooleanField()