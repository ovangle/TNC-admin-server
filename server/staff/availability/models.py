from django.db import models

from .availability_hours import AvailableHours

class Availability(models.Model):
    """
    Represents the work hours for the days of the week that a user has specified that
    they are available to work.

    Does not represent the hours actually worked
    """

    mon_available = models.BooleanField(default=False)
    mon_start = models.TimeField(null=True, default=None)
    mon_end = models.TimeField(null=True, default=None)

    tue_available = models.BooleanField(default=False)
    tue_start = models.TimeField(null=True, default=None)
    tue_end = models.TimeField(null=True, default=None)

    wed_available = models.BooleanField(default=False)
    wed_start = models.TimeField(null=True, default=None)
    wed_end = models.TimeField(null=True, default=None)

    thu_available = models.BooleanField(default=False)
    thu_start = models.TimeField(null=True, default=None)
    thu_end = models.TimeField(null=True, default=None)

    fri_available = models.BooleanField(default=False)
    fri_start = models.TimeField(null=True, default=None)
    fri_end = models.TimeField(null=True, default=None)

    def _get_hours(self, day_prefix):
        available = getattr(self, '{0}_available'.format(day_prefix))
        if not available:
            return None
        start_time = getattr(self, '{0}_start'.format(day_prefix))
        end_time = getattr(self, '{0}_end'.format(day_prefix))
        return AvailableHours(start=start_time, end=end_time)

    def _set_hours(self, day_prefix, available_hours):
        setattr(self, '{0}_available'.format(day_prefix), available_hours is None)
        if available_hours is None:
            return
        setattr(self, '{0}_start'.format(day_prefix), available_hours.start)
        setattr(self, '{0}_end'.format(day_prefix), available_hours.end)

    mon_hours = property(
        lambda self: self._get_hours('mon'), 
        lambda self, value: self._set_hours('mon', value)
    )

    tue_hours = property(
        lambda self: self._get_hours('tue' ), 
        lambda self, value: self._set_hours('tue', value)
    )

    wed_hours = property(
        lambda self: self._get_hours('wed'), 
        lambda self, value: self._set_hours('wed', value)
    )

    thu_hours = property(
        lambda self: self._get_hours('thu'), 
        lambda self, value: self._set_hours('thu', value)
    )

    fri_hours = property(
        lambda self: self._get_hours('fri'), 
        lambda self, value: self._set_hours('fri', value)
    )


