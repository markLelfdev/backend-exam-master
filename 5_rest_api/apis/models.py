from django.db import models
# Create your models here.
class School(models.Model):
    id_school = models.AutoField(primary_key=True)
    name_school = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    address = models.TextField()
    def __str__(self):
        return self.name_school

class Classroom(models.Model):
    id_class = models.AutoField(primary_key=True)
    grade_class = models.IntegerField(null=False)
    room_class = models.IntegerField(null=False)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.grade_class} / {self.room_class}'

class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    name_teacher = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    gender = models.CharField(max_length=20,null=False)
    classroom = models.ManyToManyField(Classroom,related_name='teachers')
    def __str__(self):
        return f'{self.name_teacher} {self.last_name}'

class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    name_student = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20,null=False)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_student} {self.last_name}'