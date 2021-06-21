from rest_framework import generics
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from .models import Student, Teacher, Batch

# CREATE API VIEW
class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherCreateApi(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchCreateApi(generics.CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

# LIST API VIEW
class StudentApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherApi(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchApi(generics.ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer