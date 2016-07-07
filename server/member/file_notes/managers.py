from django.db import models

from .severity import Severity

class FileNoteManager(models.Manager):
    def create(self, staff, member, message, severity=Severity.info):
        return super(FileNoteManager, self).create(
            staff=staff,
            member=member,
            message=message,
            severity=severity
        )
