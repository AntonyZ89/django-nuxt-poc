from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Discipline, Student, Teacher, DisciplineStudent
from ..serializers.discipline_student import DisciplineStudentSerializer
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from django.utils.translation import gettext_lazy as _


class _TeacherObjSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class DisciplineSerializer (FlexFieldsModelSerializer):
    total_students = serializers.SerializerMethodField()
    teacher_obj = serializers.SerializerMethodField()

    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.extra_kwargs = {
                'teacher': {
                    'error_messages': {
                        'does_not_exist': _(
                            "User doesn't exist or isn't a %(role)s."
                        )
                        %
                        {"role": _("Teacher")}
                    }
                }
            }

        model = Discipline
        fields = '__all__'
        expandable_fields = {
            'students': (serializers.SerializerMethodField)
        }

    @extend_schema_field(OpenApiTypes.INT)
    def get_total_students(self, obj: Discipline):
        query = Student.objects.filter(
            disciplinestudent__discipline__pk=obj.pk
        )

        return query.count()

    @extend_schema_field(_TeacherObjSerializer)
    def get_teacher_obj(self, obj: Discipline):
        teacher = Teacher.objects.get(pk=obj.teacher_id)

        return dict(id=teacher.id, name=teacher.name)

    @extend_schema_field(DisciplineStudentSerializer(many=True))
    def get_students(self, obj: Discipline):
        query = DisciplineStudent.objects.filter(discipline__pk=obj.pk)

        return DisciplineStudentSerializer(query, many=True).data
