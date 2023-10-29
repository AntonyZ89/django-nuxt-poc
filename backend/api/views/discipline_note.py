from rest_framework import viewsets, permissions, mixins
from api.serializers import DisciplineNoteSerializer
from api.models import DisciplineNote


class DisciplineNoteView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineNoteSerializer
    queryset = DisciplineNote.objects.all()
