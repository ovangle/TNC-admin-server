from django.db import models

class RoleManager(models.Manager):
    """
    A manager for models which can be attached to multiple types.

    The model that this Manager manages should have a `role` field, 
    which can be set to a related model's kind. 

    For example, Members, NonMemberPartners and Dependents all have 
    a `Name`, but when we are searching members by name, we often don't want 
    dependent names to appear in the list of results.

    The member automatically sets the role when creating instances, 
    based on the implementation of the `model_kind` property, and 
    overrides `get_queryset` to filter out the role.
    """

    @property
    def model_kind(self):
        raise NotImplementedError()

    def get_queryset(self):
        model_kind = self.model_kind
        qs = super(RoleManager, self).get_queryset()
        return qs.filter(role=model_kind)

    def create(self, **kwargs):
        kwargs['role'] = self.model_kind
        return super(RoleManager, self).create(**kwargs)

