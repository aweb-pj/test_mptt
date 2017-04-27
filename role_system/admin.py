from django.contrib import admin
from role_system.models import Student, Teacher


# Register your models here.
# migrate database before editing this
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','password','student_id',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','password','teacher_id',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
