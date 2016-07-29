from django.db import models

class Carer(models.Model):
    """
    A carer simply acts as an abstraction interface for a "dependent container"
    Both members and their partners can both have dependents which they may care for,
    so the carer acts as a container model for the dependents
    """
    kind = 'member::Carer'

    @property
    def name(self):
        return self.carer.name

