from django.db import models


class Address(models.Model):
    kind = 'member.basic::Address'

    street = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=4)

    def __eq__(self, address):
        if address is None:
            return False
        if address is self:     
            return True
        return all([
            self.street == address.street,
            self.city == address.city,
            self.postcode == address.postcode
        ])

