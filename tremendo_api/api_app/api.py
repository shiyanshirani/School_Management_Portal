from rest_framework import generics
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from .models import Student, Teacher, Batch

# Create API View
class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherCreateApi(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchCreateApi(generics.CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

# List API View
class StudentApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherApi(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchApi(generics.ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

# Update API View
class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

# Delete API View
class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherDeleteApi(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class BatchDeleteApi(generics.DestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer