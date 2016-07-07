from rest_framework import serializers
from ext.rest_framework.fields import EnumField
from ext.rest_framework.serializers import GenericSerializer

from ..basic.gender import Gender
from ..basic.serializers import NameSerializer, ContactSerializer, IncomeSerializer

from .models import MemberPartner, NonMemberPartner

class PartnerSerializer(GenericSerializer):

    @property
    def subkinds(self):
        subkinds = {
            MemberPartner.kind: MemberPartnerSerializer,
            NonMemberPartner.kind: NonMemberPartnerSerializer
        }

class MemberPartnerSerializer(PartnerSerializer):
    ## The id of the member that the source member is a partner of.
    partner_id = serializers.IntegerField(source='partner.pk')

class NonMemberPartnerSerializer(PartnerSerializer):
    name = NameSerializer()
    gender = EnumField(enum_type=Gender)
    contact = ContactSerializer()
    income = IncomeSerializer()

