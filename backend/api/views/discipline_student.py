from rest_framework import viewsets, permissions
from api.serializers import DisciplineStudentSerializer
from api.models import DisciplineStudent


class DisciplineStudentView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineStudentSerializer
    queryset = DisciplineStudent.objects.all()
