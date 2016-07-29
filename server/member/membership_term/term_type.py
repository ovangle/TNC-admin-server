from enum import Enum

class MembershipTermType(Enum):
    temporary = 'TEMPORARY'
    associate = 'ASSOCIATE'
    general = 'GENERAL'
    # Used only for signing up a partner of a member
    # The partner membership type expires immediately after issue
    partner = 'PARTNER'