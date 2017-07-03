from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ChemistPrescription(models.Model):
    name = models.CharField(max_length=128)

    value = models.DecimalField(max_digits=9, decimal_places=2)

    recipient_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    recipient_id = models.PositiveIntegerField()

    recipient = GenericForeignKey('recipient_type', 'recipient_id')

    @property
    def recipient_kind(self):
        from member.models import Member, Dependent
        model_class = self.recipient_type.model_class() 
        if model_class is Member:
            return Member.kind
        elif model_class is Dependent:
            return Dependent.kind
        else:
            raise TypeError('Invalid recipient kind: {0}'.format(model_class))

    @property
    def recipient_kind_id(self):
        return {
            'kind': self.recipieint_kind,
            'id': self.recipient_id
        }
