from enum import Enum 

class ResidentialStability(Enum):
    not_disclosed = 'NOT_DISCLOSED'
    no_fixed_address = 'NO_FIXED_ADDRESS'
    temporary = 'TEMPORARY'
    permanent = 'PERMANENT'