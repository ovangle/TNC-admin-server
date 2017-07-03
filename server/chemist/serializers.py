from rest_framework import serializers

from member.models import Member, Dependent

class RecipientSerializer(serializers.Serializer):
    kind = serializers.CharField()
    id = serializers.IntegerField()

    def _validate_kind(self, kind):
        if kind == Member.kind:
            return Member 
        elif kind == Dependent.kind:
            return Dependent
        else:
            raise serializers.ValidationError(
                'A ChemistPrescription can only be recieved by a Member or Dependent'
            )    

class ChemistPrescriptionSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=9, decimal_places=2)

    recipient = RecipientSerializer(source='recipient_kind_id')

    def validate(self, data):
        member = data.get('member')
        if member is None:
            raise ValueError('Member must be provided in context')

        recipient_data = data['recipient']
        try:
            recipient = get_member_or_dependent(
                recipient_data.get('kind'), 
                recipient_data.get('id')
            )     
        except ValueError as e:
            raise serializers.ValidationError(e.message)
        except models.DoesNotExist:
            raise serializers.ValidationError('recipient does not exist')

        if not member.is_partner_or_dependent(recipient):
            raise serializers.ValidationError(
                'recipient must be a partner or dependent of the submitting member'
            )

        data['recipient'] = recipient  
        return data

    def create(self, data):
        prescription = ChemistPrescription(
            recipient=data['recipient'],
            value=data['value']
        )
        return prescription








