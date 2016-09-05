from urllib.parse import urlencode
import json

from dateutil.parser import parse as parse_date
import requests

from member.models import Member
from member.basic.models import (
    Address, Contact, Gender, Name, 
    Income, IncomeType, BenefitType, ProofOfLowIncome,
    ResidentialStatus, ResidenceType, ResidentialStability
)
from member.dependent.models import Carer
from member.membership_term.models import (
    MembershipTerm, MembershipTermType, membership_expires
)


ZC_AUTHTOKEN = '11020d25f48eba54c45cd56f58b63174'
ZC_OWNERNAME = 'kyliehopkins'

APPLICATION_LINK_NAME = 'membership-database'

def view_url(view_link):
    raw_url = 'https://creator.zoho.com/api/json/{app_link}/view/{view_link}'
    return raw_url.format(
        app_link=APPLICATION_LINK_NAME,
        view_link=view_link
    )

def create_name(first_name, last_name):
    name = Name(
        role=Member.objects.kind, 
        first_name=first_name, 
        last_name=last_name
    )
    name.save()
    return name

def create_address(street_name, suburb, postcode):
    address = Address(postcode=postcode)
    address.save()
    return address

def create_contact(primary_phone, secondary_phone, email):
    def is_mobile(phone):
        return phone.startswith('04')
    home_phone = primary_phone if not is_mobile(primary_phone) else secondary_phone      
    mobile = primary_phone if is_mobile(primary_phone) else secondary_phone
    contact = Contact(phone=home_phone, mobile=mobile, email=email)
    contact.save()
    return contact

def create_income(zc_income_type, zc_proof_of_low_income, zc_benefit_type):
    benefit_type = get_centrelink_benefit_type(zc_benefit_type)
    benefit_other_description = None
    if benefit_type is BenefitType.other:
        benefit_other_description = zc_benefit_type
    income = Income(
        type=get_income_type(zc_income_type),
        proof_of_low_income=get_proof_of_low_income_value(zc_proof_of_low_income),
        benefit_type=benefit_type,
        benefit_other_description=benefit_other_description
    )
    income.save()
    return income

def create_membership_term(zc_type, joined, renewed):
    term = MembershipTerm(
        type=get_membership_term_type_value(zc_type),
        joined=get_date_value(joined),
        renewed=get_date_value(renewed)
    )
    term.expires = membership_expires(term.type, term.joined, term.renewed)
    term.save()
    return term

def create_residential_status(zc_type):
    residential_status = ResidentialStatus(
        type=get_residence_type_value(zc_type), 
        stability=get_residential_stability_value(zc_type)
    )
    residential_status.save()
    return residential_status


def get_residence_type_value(zc_type): 
    if zc_type == 'Own Home':
        return ResidenceType.own_home
    elif zc_type == 'Not Disclosed':
        return ResidenceType.not_disclosed
    elif zc_type.startswith('Private Rental'):
        if 'real estate' in zc_type:
            return ResidenceType.private_rental_real_estate
        elif 'landlord' in zc_type:
            return ResidenceType.private_rental_landlord
    elif zc_type.startswith('Public Housing'):
        return ResidenceType.public_housing
    elif zc_type.startswith('Community Housing'):
        return ResidenceType.community_housing
    elif zc_type.startswith('Homeless'):
        return ResidenceType.none
    elif zc_type.startswith('Boarding'):
        return ResidenceType.boarding
    elif zc_type.startswith('Caravan Park'):
        return ResidenceType.caravan_park
    raise ValueError('Invalid value for residence type: \'{0}\''.format(zc_type))

# For Migration purposes only
PERMANENT_RESIDENCE_TYPES = {
    ResidenceType.own_home, 
    ResidenceType.private_rental_landlord,
    ResidenceType.private_rental_real_estate,
    ResidenceType.public_housing, 
    ResidenceType.community_housing
}

TEMPORARY_RESIDENCE_TYPES = {
    ResidenceType.motel,
    ResidenceType.caravan_park,
    ResidenceType.boarding
}

NO_FIXED_ADDRESS_TYPES = {
    ResidenceType.boarding,
    ResidenceType.none,

}


def get_residential_stability_value(zc_type):
    residence_type = get_residence_type_value(zc_type)

    if residence_type == ResidenceType.not_disclosed: 
        return ResidentialStability.not_disclosed
    elif residence_type in PERMANENT_RESIDENCE_TYPES:
        return ResidentialStability.permanent
    elif residence_type in TEMPORARY_RESIDENCE_TYPES:
        return ResidentialStability.temporary
    elif residence_type in NO_FIXED_ADDRESS_TYPES:
        return REsidentialStability.no_fixed_address
    raise ValueError('Invalid value for residence type: \'{0}\''.format(zc_type))


def get_membership_term_type_value(zc_member_term):
    if not zc_member_term or zc_member_term == 'Temporary':
        return MembershipTermType.temporary
    elif zc_member_term == 'Associate':
        return MembershipTermType.associate
    elif zc_member_term in {'Staff', 'General'}:
        return MembershipTermType.General
    else:
        raise ValueError('Invalid value for zc_member_term: \'{0}\''.format(zc_member_term))

def get_date_value(zc_date):
    if not zc_date:
        return None
    return parse_date(zc_date, yearfirst=False, dayfirst=True)

def get_centrelink_benefit_type(zc_value):
    if not zc_value: 
        return BenefitType.not_disclosed
    elif zc_value == 'None':
        return BenefitType.none
    elif zc_value == 'Disability':
        return BenefitType.disability
    elif zc_value == 'Aged':
        return BenefitType.aged
    elif zc_value == 'Carer':
        return BenefitType.carer
    elif zc_value == 'Newstart':
        return BenefitType.newstart
    elif zc_value == 'Youth Allowance':
        return BenefitType.youth_allowance
    elif zc_value == 'FTB':
        return BenefitType.abstudy
    elif zc_value == 'PPP':
        return BenefitType.parenting_payment_partnered
    elif zc_value == 'PPS':
        return BenefitType.parenting_payment_single
    elif zc_value == 'Abstudy':
        return BenefitType.abstudy
    elif zc_value == 'Austudy':
        return BenefitType.austudy
    else:
        # Other benefit type
        return BenefitType.other

def get_income_type(zc_income_type):
    if not zc_income_type:
        return IncomeType.none
    elif zc_income_type == 'Full-time Employment':
        return IncomeType.not_disclosed
    elif zc_income_type == 'Part-time/Casual Employment':
        return IncomeType.partially_employed
    elif zc_income_type == 'Self-Employment':
        return IncomeType.self_employed
    elif zc_income_type == 'Centrelink Benefit':
        return IncomeType.centrelink_benefit
    elif zc_income_type == 'Self-funded Retiree':
        return IncomeType.self_funded_retiree
    elif zc_income_type == 'Veterans affairs':
        return IncomeType.not_disclosed
    else:
        raise ValueError('Invalid value for zc_income_type: \'{0}\''.format(zc_income_type))

def get_gender_value(zc_gender):
    if not zc_gender or zc_gender == 'Not disclosed':
        return Gender.not_disclosed
    elif zc_gender == 'Female':
        return Gender.female
    elif zc_gender == 'Male':
        return Gender.male
    else:
        raise ValueError('Invalid value for zc_gender: \'{0}\''.format(zc_gender))

def get_aboriginal_or_torres_strait_islander_value(zc_value):
    if not zc_value or zc_value == 'Not disclosed': 
        return None
    elif zc_value == 'Yes':
        return True
    elif zc_value == 'No':
        return False
    else:
        raise ValueError('Invalid value for zc_aboriginal_or_torres_strait_islander: \'{0}\''.format(zc_value))

def get_proof_of_low_income_value(zc_value):
    if 'Health Care Card' in zc_value:
        return ProofOfLowIncome.low_income_health_care_card_sighted
    elif 'Centrelink Card' in zc_value:
        return ProofOfLowIncome.pensioner_concession_card_sighted
    else:
        return ProofOfLowIncome.no_proof

def zc_member_to_member(zc_member):
    carer = Carer()
    carer.save()

    return Member(
        id=zc_member['Member_ID'],
        name=create_name(zc_member['First_name'], zc_member['Family_name']),
        term=create_membership_term(
            zc_member['Member_Type'],
            zc_member['Joined'],
            zc_member['Renewed']
        ),
        gender=get_gender_value(zc_member['Gender']),
        date_of_birth=get_date_value(zc_member['Date_of_Birth']),
        aboriginal_or_torres_strait_islander=get_aboriginal_or_torres_strait_islander_value(
            zc_member['Aboriginal_Torres_Strait_Islander']
        ),

        address=create_address(zc_member['Street_address'], zc_member['Suburb'], zc_member['Post_Code']),
        contact=create_contact(
            zc_member['Primary_Contact_Number'], 
            zc_member['Secondary_Contact_Number1'], 
            zc_member['Primary_Email']
        ),
        income=create_income(
            zc_income_type=zc_member['Income'],
            zc_proof_of_low_income=zc_member['Proof_of_Low_Income1'],
            zc_benefit_type=zc_member['Centrelink_Benefit_Type']
        ),
        residential_status=create_residential_status(zc_member['Residential_Status']),
        carer=carer
    )

def iter_member_records(member_id, member_id_end=None):
    """
    A generate over the member records between member_id and member_id_end (inclusive).
    If member_id_end is not provided, emits the record with id member_id
    """
    criteria = 'Member_ID >= {start_range} && Member_ID <= {end_range}'.format(
        start_range=member_id,
        end_range=member_id_end or member_id
    )        

    params = {
        'authtoken': ZC_AUTHTOKEN,
        'scope': 'creatorapi',
        'zc_ownername': ZC_OWNERNAME,
        'raw': 'true',
        'criteria': criteria
    }

    r = requests.get(
        view_url('Old_Member_Database_View'),
        params=params
    )

    print('Fetching {0}'.format(r.url))

    response_data = r.json()['Member_details']

    for item in response_data:
        yield item

def migrate_member_ids(member_id, member_id_end=None):
    for zc_member in iter_member_records(member_id, member_id_end):
        member = zc_member_to_member(zc_member)
        member.save()
   

if __name__ == '__main__':
    for member in iter_member_records(100041):
        print(item)
