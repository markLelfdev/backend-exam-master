from rest_framework import viewsets
from ...models import Student
from ...serializers import StudentSerializer
from ...filters import StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
