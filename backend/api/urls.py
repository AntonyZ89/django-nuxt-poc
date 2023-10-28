from rest_framework import routers
from django.urls import path
from .views import (
    auth, discipline, discipline_note, discipline_student
)

router = routers.DefaultRouter()

router.register('discipline', discipline.DisciplineView)
router.register('discipline-note', discipline_note.DisciplineNoteView)
router.register('discipline-student', discipline_student.DisciplineStudentView)

auth_urls = [
    path("login", auth.login),
    path("signup", auth.signup),
]

user_urls = []

urlpatterns = router.urls + user_urls + auth_urls
