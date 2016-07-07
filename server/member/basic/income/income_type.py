from enum import Enum

class IncomeType(Enum):
    none = 'NONE' 
    not_disclosed = 'NOT_DISCLOSED'
    centrelink_benefit = 'CENTRELINK_BENEFIT'
    partially_employed = 'PARTIALLY_EMPLOYED'
    fully_employed = 'FULLY_EMPLOYED'
    self_employed = 'SELF_EMPLOYED'
    self_funded_retiree = 'SELF_FUNDED_RETIREE'