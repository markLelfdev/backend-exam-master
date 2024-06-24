from django.contrib import admin
from .models import Classroom,School,Student,Teacher

# Register your models here.


class School_admin(admin.ModelAdmin):
    list_display = ('id_school','name_school','short_name','address')
    readonly_fields = ('id_school',)
    fields = ('id_school','name_school','short_name','address')

class Classroom_admin(admin.ModelAdmin):
    list_display = ('id_class','grade_class','room_class','school')
    readonly_fields = ('id_class',)
    fields = ('id_class','grade_class','room_class','school')

class Teacher_admin(admin.ModelAdmin):
    list_display = ('id_teacher','name_teacher','last_name','gender')
    readonly_fields = ('id_teacher',)
    fields = ('id_teacher','name_teacher','last_name','gender','classroom')

class Student_admin(admin.ModelAdmin):
    list_display = ('id_student','name_student','last_name','gender','classroom')
    readonly_fields = ('id_student',)
    fields = ('id_student','name_student','last_name','gender','classroom')

admin.site.register(School,School_admin)
admin.site.register(Classroom,Classroom_admin)
admin.site.register(Student,Student_admin)
admin.site.register(Teacher,Teacher_admin)
