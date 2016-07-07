from rest_framework.serializers import (
    Field, RegexField, ValidationError
)

import re

class EnumField(Field):
    def __init__(self, **kwargs):
        self.enum_type = kwargs.pop('enum_type')
        if (self.enum_type is None):
            raise ValueError('Must provide an enumeration type as \'enum_type\'')
        super(EnumField, self).__init__(**kwargs)    

    def to_representation(self, obj):       
        return obj.value

    def to_internal_value(self, obj):     
        try:
            return self.enum_type(obj)
        except ValueError:    
            raise ValidationError(
                'Could not serialize {0} as enum value of {1}'
                .format(obj, self.enum_type)
            )
