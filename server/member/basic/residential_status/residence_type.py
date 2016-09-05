from enum import Enum

class ResidenceType(Enum):
    not_disclosed = 'NOT_DISCLOSED'
    none = 'NONE'
    caravan_park = 'CARAVAN_PARK'
    motel = 'MOTEL'
    boarding = 'BOARDING'
    private_rental_landlord = 'PRIVATE_RENTAL_LANDLORD'
    private_rental_real_estate = 'PRIVATE_RENTAL_REAL_ESTATE'
    public_housing = 'PUBLIC_HOUSING'
    community_housing = 'COMMUNITY_HOUSING'
    own_home = 'OWN_HOME'