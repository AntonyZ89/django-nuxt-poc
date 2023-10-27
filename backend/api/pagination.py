from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'per_page': self.page.paginator.per_page,
            'page': self.page.number,
            'pages': self.page.paginator.num_pages,
            'results': data
        })
