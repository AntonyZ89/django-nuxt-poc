from rest_framework import viewsets, permissions
from api.serializers import DisciplineNoteSerializer
from api.models import DisciplineNote


class DisciplineNoteView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineNoteSerializer
    queryset = DisciplineNote.objects.all()
