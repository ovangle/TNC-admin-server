from django.db import models

from django.contrib.postgres.fields import ArrayField 

class StaffInductionSurvey(models.Model):
    """
    This is the form that we ask users to fill out when joining the centre.
    """

    has_previous_experience = models.BooleanField()

    skills = ArrayField(
        models.CharField(max_length=32),
        default=list
    )

    traits = ArrayField(
        models.CharField(max_length=32),
        default=list
    )

    date_available_to_start = models.DateField()
    desired_hours_per_week = models.SmallIntegerField()
    referred_by = models.CharField(max_length=64)

    has_understood_privacy_obligations = models.BooleanField()




