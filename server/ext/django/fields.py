from enum import Enum
from django.db.models import Field, CharField

def is_valid_enum_type(enum_type): 
    return (enum_type is not None
        and isinstance(enum_type, type)
        and Enum in enum_type.__mro__
    )

def enum_choices(enum_type):
    return [(k, v.value) for k, v in enum_type.__members__.items()]


class EnumField(Field):
    description = 'Enumerated values of type %(enum_type)s'

    def __init__(self, **kwargs):
        self.enum_type = kwargs.pop('enum_type')           
        if not is_valid_enum_type(self.enum_type):
            raise ValueError(
                "'enum_type' must be provided and be a subclass of 'enum.Enum'"
            )
        self.max_length = kwargs.setdefault('max_length', 32)    
        kwargs.setdefault('choices', enum_choices(self.enum_type))
        super(EnumField, self).__init__(**kwargs) 

    def db_type(self, connection):      
        return 'varchar({0})'.format(self.max_length)

    def deconstruct(self):     
        name, path, args, kwargs = super(EnumField, self).deconstruct()
        kwargs['enum_type'] = self.enum_type
        return name, path, args, kwargs

    def get_prep_value(self, value): 
        if value is None:
            return ''
        if isinstance(value, self.enum_type):
            value = value.value
        return value    

    def from_db_value(self, value, expression, connection, context):
        if not value:
            return None
        if value and not isinstance(value, self.enum_type):
            value = self.enum_type(value)
        return value     

