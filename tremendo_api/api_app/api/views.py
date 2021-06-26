from django.shortcuts import render
from api_app.serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from api_app.models import Student, Teacher, Batch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class StudentList(APIView):
    """
    List all students, or create a new student
    """
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    """
    Retrieve, update or delete a student
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response({"Error": "Student does not exist."}, status=status.HTTP_400_BAD_REQUEST) # doubt

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherList(APIView):
    """
    List all teachers, or create a new teacher. 
    """
    def get(self, request):
        teachers = Teacher.objects.all()
        serializers = TeacherSerializer(teachers, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherDetail(APIView):
    """
    Retrieve, update or delete a teacher.
    """
        
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({"Error": "Teacher does not exist"}, status=status.HTTP_400_BAD_REQUEST)  # doubt
        
    def get(self, request, pk):
        teacher = self.get_object(pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        teacher = self.get_object(pk=pk)
        teacher.delete()
        return Response({"Success": "Teacher is deleted."}, status=status.HTTP_200_OK)



class BatchList(APIView):
    """
    List all batch.
    """
    def get(self, request):
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)