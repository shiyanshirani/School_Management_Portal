from django.shortcuts import render
from django.core.paginator import Paginator

from api_app.serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from api_app.models import Student, Teacher, Batch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentList(APIView):
    """
    List all students, or create a new student
    """
    # def get(self, request):
    #     students = Student.objects.all()
    #     serializer = StudentSerializer(serializer.data, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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
            return Response("Student does not exist.", status=status.HTTP_400_BAD_REQUEST) # doubt

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
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)  # doubt
        
    def get(self, request, pk):
        try:
            teacher = self.get_object(pk=pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk):
        try:
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            teacher = self.get_object(pk=pk)
            teacher.delete()
            return Response({"Success": "Teacher is deleted."}, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "TeacherID: {} does not exist".format(pk)}, status=status.HTTP_400_BAD_REQUEST)



class BatchList(APIView):
    """
    List all batch
    """
    def get(self, request):
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BatchDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Batch.objects.get(pk=pk)
        except Batch.DoesNotExist:
            return Response({"Error": "Batch does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        try:
            batch = self.get_object(pk)
            serializer = BatchSerializer(batch)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "Batch does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination

class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = PageNumberPagination

class BatchListView(ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    pagination_class = PageNumberPagination