from django.db import models


class Address(models.Model):
    kind = 'member.basic::Address'

    street = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=4)

