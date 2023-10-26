from .student import StudentSerializer
from .teacher import TeacherSerializer
from .coordinator import CoordinatorSerializer
from .discipline import DisciplineSerializer
from .discipline_note import DisciplineNoteSerializer
from .discipline_student import DisciplineStudentSerializer

__all__ = [
    "StudentSerializer",
    "TeacherSerializer",
    "CoordinatorSerializer",
    "DisciplineSerializer",
    "DisciplineNoteSerializer",
    "DisciplineStudentSerializer",
]
