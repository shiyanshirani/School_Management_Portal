from django.shortcuts import render
from api_app.serializers import StudentSerializer, TeacherSerializer, BatchSerializer
from api_app.models import Student, Teacher, Batch
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])  # GET all and POST
def student(request):
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
def student_api(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response("Student does not exist." ,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
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
def teacher(request):
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
def teacher_api(request, pk):
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
            "batches": batches.values('students', 'teacher', 'total_classes', 'completed_classes')
        }
        # serializer = BatchSerializer(batches, many=True)
        return Response(context, status=status.HTTP_200_OK)

# class BatchViewSet(viewsets.ModelViewSet):
#     serializer_class = BatchSerializer

#     def get_queryset(self):
#         batch = Batch.objects.all()
#         return batch