from django.db import models

class Contact(models.Model):
    kind = 'member.basic::Contact'

    email = models.EmailField(default='')
    phone = models.CharField(max_length=10, default='')
    mobile = models.CharField(max_length=10, default='')