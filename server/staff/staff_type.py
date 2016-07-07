from enum import Enum

class StaffType(Enum):
    """
    The user type is a quick reference for how the system should treat the user.

    It has nothing to do with the permissions a user has in the system
    """
    
    # A permanent staff member of the facility
    PermanentStaff = 'PERMANENT_STAFF'

    # A volunteer who works in the office 
    OfficeVolunteer = 'OFFICE_VOLUNTEER'

    # A volunteer who works at foodcare
    FoodcareVolunteer = 'FOODCARE_VOLUNTEER'

    # Some other volunteer who was granted access to the system
    OtherVolunteer = 'OTHER_VOLUNTEER'

