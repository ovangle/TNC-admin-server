from django.db import models

from .severity import Severity

class FileNoteManager(models.Manager):
    kind = 'member.filenote::FileNote'

    def create(self, staff, member_id, message, severity=Severity.info):
        return super(FileNoteManager, self).create(
            staff=staff,
            member_id=member_id,
            message=message,
            severity=severity
        )
