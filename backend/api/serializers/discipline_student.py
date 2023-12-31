from rest_framework import serializers
from ..models import DisciplineStudent
from django.utils.translation import gettext as _


class DisciplineStudentSerializer (serializers.ModelSerializer):
    user_obj = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()

    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.extra_kwargs = {
                'user': {
                    'error_messages': {
                        'does_not_exist': _(
                            "User doesn't exist or isn't a %(role)s."
                        )
                        %
                        {"role": _("Teacher")}
                    }
                },
                'note_1': {
                    'min_value': 0,
                    'max_value': 10
                },
                'note_2': {
                    'min_value': 0,
                    'max_value': 10
                }
            }

        model = DisciplineStudent
        fields = '__all__'

    def get_media(self, obj: DisciplineStudent):
        if obj.note_1 is None and obj.note_2 is None:
            return None

        note_1 = obj.note_1 or 0
        note_2 = obj.note_2 or 0
        return (note_1 + note_2) / 2

    def get_user_obj(self, obj: DisciplineStudent):
        user = obj.user

        return dict(id=user.id, name=user.name)
