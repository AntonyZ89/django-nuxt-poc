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

    def get_paginated_response_schema(self, schema):
        res = super().get_paginated_response_schema(schema)
        results = res['properties']['results']

        res['properties']['count']['example'] = 20
        res['properties'][self.page_size_query_param] = dict(
            type='integer',
            example=self.page_size
        )
        res['properties']['page'] = dict(type='integer', example=10)
        res['properties']['pages'] = dict(type='integer', example=10)

        del res['properties']['results']

        # reorder `results`
        res['properties']['results'] = results

        del res["properties"]["next"]
        del res["properties"]["previous"]

        return res
