from rest_framework import serializers
from .models import School,Classroom,Teacher,Student
# หน้าการแสดงผล Json
class SchoolSerializer(serializers.ModelSerializer):
    count_classroom = serializers.SerializerMethodField()
    count_teacher = serializers.SerializerMethodField()
    count_student = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = ['id_school', 'name_school','short_name','address','count_classroom', 'count_teacher', 'count_student']
    def get_count_classroom(self, obj):
        return Classroom.objects.filter(school=obj).count()
    def get_count_teacher(self, obj):
        classrooms = Classroom.objects.filter(school=obj)
        return Teacher.objects.filter(classroom__in=classrooms).distinct().count()
    def get_count_student(self, obj):
        classrooms = Classroom.objects.filter(school=obj)
        return Student.objects.filter(classroom__in=classrooms).count()
    
    
class ClassroomSerializer(serializers.ModelSerializer):
    school_name = serializers.SerializerMethodField()
    grade_and_room = serializers.SerializerMethodField()
    list_of_teachers = serializers.SerializerMethodField()
    list_of_students = serializers.SerializerMethodField()
    class Meta:
        model = Classroom
        fields = ['id_class','grade_class', 'room_class','school','school_name','grade_and_room', 'list_of_teachers', 'list_of_students']        
    def get_school_name(self,obj):
        return obj.school.name_school
    def get_grade_and_room(self,obj):
        return f'{obj.grade_class}/{obj.room_class}'
    def get_list_of_teachers(self, obj):
        teachers = Teacher.objects.filter(classroom=obj).distinct()
        return [{"id_teacher": teacher.id_teacher, "name_teacher": teacher.name_teacher, "last_name": teacher.last_name} for teacher in teachers]
    def get_list_of_students(self, obj):
        students = Student.objects.filter(classroom=obj)
        return [{"id_student": student.id_student, "name_student": student.name_student, "last_name": student.last_name} for student in students]

class TeacherSerializer(serializers.ModelSerializer):
    list_of_classrooms = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ['id_teacher', 'name_teacher', 'last_name', 'gender',
                  'classroom','list_of_classrooms' ]
    def get_list_of_classrooms(self, obj):
        classrooms = obj.classroom.all()
        return [f"{classroom.grade_class}/{classroom.room_class} {classroom.school.name_school}" for classroom in classrooms]

   
class StudentSerializer(serializers.ModelSerializer):
    classrooms_name = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id_student', 'name_student', 'last_name', 'gender',
                  'classrooms_name','classroom']
    def get_classrooms_name(self,obj):
        return f'{obj.classroom.grade_class}/{obj.classroom.room_class} {obj.classroom.school.name_school}'

