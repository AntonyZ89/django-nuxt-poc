from rest_framework import viewsets, permissions
from api.serializers import DisciplineSerializer
from api.models import Discipline


class DisciplineView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
