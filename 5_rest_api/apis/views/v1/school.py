from rest_framework import viewsets
from ...models import School,Classroom
from ...serializers import SchoolSerializer,ClassroomSerializer
from ...filters import SchoolFilter,ClassroomFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter
