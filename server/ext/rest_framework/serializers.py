import collections
from rest_framework import serializers

class GenericSerializer(serializers.Serializer):
    kind = serializers.CharField(max_length=32)

    @property
    def subkinds(self):
        raise NotImplementedError('`subkinds` must be implemented')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        super(GenericSerializer, self).__init__(*args, **kwargs)

    def get_serializer_for_kind(self, kind): 

        if not isinstance(self.subkinds, collections.Mapping): 
            raise TypeError('subkinds must be a maplike object')

        if not kind in self.subkinds:
            raise ValueError('invalid kind for serializer: {0}'.format(kind))

        serializer = self.subkinds[kind]
        if not issubclass(serializer, type(self)):
            raise typeerror('a serializer subkind class must be a subclass of {0}'.format(type(self)))
        return serializer

    def validate_kind(self, value):
        if not value in self.subkinds:
            raise ValidationError('Invalid kind: Must be one of {0}'.format(self.subkinds.join(', ')))
        return value 

    def to_internal_value(self, data):
        kind = data.pop('kind')
        serializer_cls = self.get_serializer_for_kind(data)

        if type(self) is serializer_cls:
            # If we've already resolved the subkind, call `super`
            return super(GenericSerializer, self).to_internal_value(data)

        serializer = serializer_cls(*self.args, **self._kwargs) 
        return serializer.to_internal_value(data)

    def to_representation(self, instance):
        if not hasattr(instance, 'kind') and not hasattr(type(instance), 'kind'):
            raise TypeError('Instances serialized by a GenericSerializer must have a \'kind\' attribute')
        serializer_cls = self.get_serializer_for_kind(instance.kind) 

        print('serializer_cls: {0}'.format(serializer_cls))

        if not hasattr(instance, 'get_subkind_instance'):
            raise TypeError('Instances serialized by a GenericSerializer must implement \'get_subkind_instance\'')
        instance = instance.get_subkind_instance()

        print('instance: {0}'.format(instance))

        if type(self) is serializer_cls:
            # If we've already resolved the subkind, call `super`
            return super(GenericSerializer, self).to_representation(instance)

        serializer = serializer_cls(*self._args, **self._kwargs)
        return serializer.to_representation(instance)
