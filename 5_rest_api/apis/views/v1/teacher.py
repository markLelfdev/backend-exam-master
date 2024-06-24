from rest_framework import viewsets
from ...models import Teacher
from ...serializers import TeacherSerializer
from ...filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter