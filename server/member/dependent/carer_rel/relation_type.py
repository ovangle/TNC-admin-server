from enum import Enum

class RelationType(Enum):
    not_disclosed = 'NOT_DISCLOSED'
    no_familial_relation = 'NO_RELATION'
    parent = 'PARENT'
    partner_of_parent = 'PARTNER_OF_PARENT'
    sibling = 'SIBLING' 
    other = 'OTHER_RELATION'
