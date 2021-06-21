from rest_framework import generics
from rest_framework.response import Response
from .serializer import StudentSerializer, TeacherSerializer, BatchSerializer
from .models import Student, Teacher, Batch

class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherCreateApi(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchCreateApi(generics.CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer