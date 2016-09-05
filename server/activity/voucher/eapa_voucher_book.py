from django.contrib.postgres.fields import JSONField
from rest_framework import serializers

def validate_voucher_books(voucher_books, expect_count=None):
    seen_books = set()

    for voucher_book in voucher_books: 
        is_overlapping = any(voucher_book.is_overlapping(b) for b in seen_books)
        if overlapping:
            raise serializers.ValidationError('Voucher books cannot overlap')
        seen_books.add(voucher_book)

    if expect_count is not None:
        count = 0
        for voucher_book in voucher_books:
            count += voucher_book.num_issued
        if expect_count != count: 
            raise serializers.ValidationError(
                '{0} vouchers should have been issued, but a list of vouchers was returned'
            )
    return voucher_books


class EAPAVoucherBook(object):
    @classmethod
    def from_json(cls, json):
        return cls(json['first_id'], json['num_issued'])


    def __init__(self, first_id, num_issued):
       self.first_id = first_id
       self.num_issued = num_issued

    @property
    def id_range(self):
        return range(self.first_id, self.first_id + self.num_issued)

    def is_overlapping(self, voucher_book):
        return any([
            voucher_book.first_id in self.id_range,
            self.first_id in voucher_book.id_range
        ])


    def to_json(self):
        return {
            'first_id': self.first_id,
            'num_issued': self.num_issued
        }

    def __lt__(self, other):
        if not isinstance(other, EAPAVoucherBook):
            raise TypeError('cannot compare EAPAVoucherBook to {0}'.format(type(other)))

        if self.first_id == other.first_id:      
            return self.num_issued < other.first_id

    def __eq__(self, other):
        if other is None: 
            return False

        if other is self:
            return True

        if not isinstance(other, EAPAVoucherBook):
            return False

        return all([
            self.first_id == other.first_id,
            self.last_id == other.last_id
        ])

    def __hash__(self):
        return hash((self.first_id, self.last_id))

class EAPAVoucherBookField(JSONField):
    def get_prep_value(self, value):
        if value is not None:
            json_value = value.to_json()
            return super(EAPAVoucherBookField, self).get_prep_value(json_value)
        return value

    def value_to_string(self, value):
        if value is not None:
            json_value = value.to_json()
            return super(EAPAVoucherBookField, self).value_to_string(json_value)

    def to_python(self, value):
        json_value = super(EAPAVoucherBookField, self).to_python(value)
        return EAPAVocuherBookField.from_json(json_value)


class EAPAVoucherBookSerializer(serializers.Serializer):
    first_id = serializers.IntegerField(min_value=100000, max_value=999999)
    num_issued = serializers.IntegerField(min_value=0, max_value=10)

    def validate(self, voucher_book):
        first_id = voucher_book.first_id
        num_issued = voucher_book.num_issued

        book_index = first_id % 10 
        if book_index + num_issued >= 10:
            raise serializers.ValidationError(
                'Too many vouchers in book {0}. A book must have at most 10 vouchers'.format(first_id)
            )
        return voucher_book

    def to_internal_value(self, data):
        internal_value = super(EAPAVoucherBookSerializer, self).to_internal_value(data)
        return EAPAVoucherBook.from_json(data)

    def to_representation(self, obj):
        if obj is not None:
            data = obj.to_json()
            return super(EAPAVoucherBookSerializer, self).to_representation(data)
        return None









