from datetime import timedelta, datetime
from django.db import models

from .term_type import MembershipTermType

def start_of_next_financial_year(date):
    year = date.year
    if date.month >= 7:
        # The end of financial year is in june the next year in months after July
        year += 1
    return datetime(year, 7, 1)

def membership_expires(membership_type, joined, renewed=None):
    membership_start = joined
    if renewed is not None:
        membership_start = renewed

    if membership_type == MembershipTermType.temporary:
        # Temporary memberships expire in 31 days
        return membership_start + timedelta(31)
    elif membership_type in {MembershipTermType.associate, MembershipTermType.general}:
        # Associate and general memberships expire at the start of the next financial year
        return start_of_next_financial_year(membership_start)
    elif membership_type == MembershipTermType.partner:
        if renewed is not None:
            raise ValueError('Cannot renew PARTNER membership type')
        return membership_start
    else:
        raise ValueError('Invalid membership term type: "{0}"'.format(type))

class MembershipTermManager(models.Manager):
    def create(self, membership_type, joined):
        return super(MembershipTermManager, self).create(
            type=membership_type,
            joined=joined,
            expires=membership_expires(membership_type, joined)
        )




