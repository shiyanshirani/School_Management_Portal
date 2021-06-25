from django.shortcuts import render
from .serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from .models import Student, Teacher, Batch
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.

# @csrf_exempt
# @api_view(['GET'])
# def get_student_by_id(request):
#     if request.method == "GET":
#         student = Student.objects.get(pk=request.POST['id'])
#         context = {
#             "Student": StudentSerializer(student).data
#         }
#     return Response(context)

@csrf_exempt
@api_view(['GET', 'POST'])  # GET all And POST
def student_operations(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])  # GET(by_id), PUT & DELETE
def student_changes(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response("Student does not exist." ,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, )
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_200_OK)

# CRUD Teacher

@csrf_exempt
@api_view(['GET', 'POST'])  # get all details and post
def teacher_operations(request):
    if request.method == "GET":
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def teacher_changes(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_200_OK)

# Batch

@api_view(['GET'])
def batch(request):
    if request.method == "GET":
        batches = Batch.objects.all()
        context = {
            "batches": batches.values('id',)
        }
        # serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class BatchViewSet(viewsets.ModelViewSet):
#     serializer_class = BatchSerializer

#     def get_queryset(self):
#         batch = Batch.objects.all()
#         return batch