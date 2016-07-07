from enum import Enum

class BenefitType(Enum):
    none = 'NONE' 
    not_disclosed = 'NOT_DISCLOSED'
    newstart = 'NEWSTART'
    aged = 'AGED'
    disability = 'DISABILITY'
    carer = 'CARER'
    youth_allowance = 'YOUTH_ALLOWANCE'
    abstudy = 'ABSTUDY'
    austudy = 'AUSTUDY'
    family_tax_benefit = 'FAMILY_TAX_BENEFIT'
    parenting_payment_partnered = 'PARENTING_PAYMENT_PARTNERED'
    parenting_payment_single = 'PARENTING_PAYMENT_SINGLE'
    other = 'OTHER'