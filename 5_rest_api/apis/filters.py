from django_filters import FilterSet, filters
from .models import School,Classroom,Student,Teacher

# code here
class SchoolFilter(FilterSet):
    name_school = filters.CharFilter(field_name='name_school'
                                     ,lookup_expr='icontains')
    class Meta:
        model = School
        fields = ['name_school']

class ClassroomFilter(FilterSet):
    school_name = filters.CharFilter(field_name='school__name_school'
                                     ,lookup_expr='icontains')
    class Meta:
        model = Classroom
        fields = []

class TeacherFilter(FilterSet):
    name_school = filters.CharFilter(field_name='school__name_school'
                                     ,lookup_expr='icontains')
    classroom = filters.CharFilter(field_name='classroom__grade_class',
                                       lookup_expr='icontains')
    firstname = filters.CharFilter(field_name='name_teacher',
                                   lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='last_name',
                                   lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender',
                                     lookup_expr='icontains')
    class Meta:
        model = Teacher
        fields = []
        
class StudentFilter(FilterSet):
    name_school = filters.CharFilter(field_name='school__name_school'
                                     ,lookup_expr='icontains')
    classroom = filters.CharFilter(field_name='classroom__grade_class',
                                       lookup_expr='icontains')
    firstname = filters.CharFilter(field_name='name_teacher',
                                   lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='last_name',
                                   lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender',
                                     lookup_expr='icontains')
    class Meta:
        model = Student
        fields = []