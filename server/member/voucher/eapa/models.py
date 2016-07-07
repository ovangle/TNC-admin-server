from django.db import models

class EAPAAssessment(models.Model):
    is_no_relation_to_assessor = models.BooleanField()  
    bill_sighted = models.BooleanField()

    is_name_on_bill = models.BooleanField()
    is_address_on_bill = models.BooleanField() 

    is_residential_electicity_or_gas_account = models.BooleanField()

    is_experiencing_financial_hardship = models.BooleanField()
    is_denying_basic_needs = models.BooleanField()
    is_facing_disconnection = models.BooleanField() 

    has_contacted_retailer_to_check_payment_plans = models.BooleanField()
    has_contacted_retailer_to_check_energy_rebates = models.BooleanField()
    has_contacted_retailer_to_check_updated_balance = models.BooleanField()
    has_contacted_retailer_to_check_eapa_payments = models.BooleanField()

    is_receiving_over_limit_on_current_bill = models.BooleanField()
    is_receiving_over_limit_for_financial_year = models.BooleanField()
    is_receiving_assistance_more_than_twice = models.BooleanField()

    limit_exemption_description = models.TextField()

    signed_privacy_agreement = models.BooleanField()

    is_bill_stamped = models.BooleanField() 

    understood_voucher_processing = models.BooleanField()

    consent_to_retain_data = models.BooleanField()