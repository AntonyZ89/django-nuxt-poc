from rest_framework import routers
from .views import (
    auth, discipline, discipline_note, discipline_student
)

router = routers.DefaultRouter()

router.register('', auth.AuthView, basename='auth')
router.register(
    'discipline',
    discipline.DisciplineView,
    basename='discipline'
)
router.register(
    'discipline-note',
    discipline_note.DisciplineNoteView,
    basename='discipline-note'
)
router.register(
    'discipline-student',
    discipline_student.DisciplineStudentView,
    basename='discipline-student'
)

urlpatterns = router.urls
