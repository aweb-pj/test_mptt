from django.shortcuts import render
from rest_framework.decorators import api_view
from role_system.models import Student, Teacher
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def student_login(request, studentid, password):
    student = Student.objects.all().filter(student_id=studentid).filter(password=password)
    if student.exists():
        student = student[0]
        result = {'login': 'successful', 'name': student.name}
        return Response(data=result)
    else:
        result = {'login': 'failure'}
        return Response(data=result,status=status.HTTP_404_NOT_FOUND)


