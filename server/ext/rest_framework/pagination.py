from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class PageIdPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('last_page', not self.page.has_next()),
            ('page_id', self.page.number),
            ('items', data)
        ]))
