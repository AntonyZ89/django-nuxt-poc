from rest_framework import routers
from .views import (
    auth, discipline, discipline_student, user
)

router = routers.DefaultRouter()

router.register('', auth.AuthView, basename='auth')
router.register('user', user.UserView)
router.register(
    'discipline',
    discipline.DisciplineView,
    basename='discipline'
)
router.register(
    'discipline-student',
    discipline_student.DisciplineStudentView,
    basename='discipline-student'
)

urlpatterns = router.urls
