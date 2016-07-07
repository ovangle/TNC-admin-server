from datetime import datetime

from rest_framework import serializers

class AvailableHours(object):
    def __init__(self, start=None, end=None):
        self.start = start 
        self.end = end 

        if self.start is not None and self.end is not None and self.start > self.end:
            raise ValueError('End time cannot preceed start time')

        super(AvailabilityHours, self).__init__()

class AvailableHoursField(serializers.Field):
    def to_representation(self, value):
        if value is None:
            return value

        repr_start, repr_end = '*', '*'
        if value.start is not None:
            repr_start = value.start.strftime('%H:%M')
        if value.end is not None:
            repr_end = value.end.strftime('%H:%M')
        return [repr_start, repr_end]

    def to_internal_value(self, value):
        if value is None:
            return value

        value = list(value)
        if len(value) != 2:
            raise ValueError(
                'Value must be a list with two elements, representing the start and end of the interval. '
                'Either value can be \'*\', representing any start/end time.'
            )

        raw_start, raw_end = value
        start, end = None, None

        if raw_start != '*':
            start = datetime.strptime(raw_start, '%H:%M').time()
        if raw_end != '*':
            end = datetime.datetime.strptime(raw_end, '%H:%M').time()

        return AvailabilityHours(start, end)











