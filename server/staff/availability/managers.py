

class UserAvailabilityManager(models.Manager):

    def create(self, **kwargs):
        availability = UserAvailability()
        availability.mon_hours = kwargs.pop('mon', None)
        availability.tue_hours = kwargs.pop('tue', None)
        availability.wed_hours = kwargs.pop('wed', None)
        availability.thu_hours = kwargs.pop('thu', None)
        availability.fri_hours = kwargs.pop('fri', None)
        return availability.save()

    def update(self, instance, **kwargs):
        instance.mon_hours = kwargs.pop('mon', instance.mon_hours) 
        instance.tue_hours = kwargs.pop('tue', instance.tue_hours)
        instance.wed_hours = kwargs.pop('wed', instance.wed_hours)
        instance.thu_hours = kwargs.pop('thu', instance.thu_hours)
        instance.fri_hours = kwargs.pop('fri', instance.fri_hours)
        return availbility.save()

