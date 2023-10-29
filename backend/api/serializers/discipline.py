from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Discipline, Student, Teacher
from ..serializers import StudentSerializer
from drf_spectacular.utils import extend_schema_field, OpenApiTypes


class _TeacherObjSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class DisciplineSerializer (FlexFieldsModelSerializer):
    total_students = serializers.SerializerMethodField()
    teacher_obj = serializers.SerializerMethodField()

    class Meta:
        model = Discipline
        fields = '__all__'
        extra_kwargs = {
            'teacher': {
                'error_messages': {
                    'does_not_exist': "User doesn't exist or isn't a Teacher."
                }
            }
        }
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

    def get_students(self, obj: Discipline):
        query = Student.objects.filter(
            disciplinestudent__discipline__pk=obj.pk
        )

        return StudentSerializer(query, many=True).data
