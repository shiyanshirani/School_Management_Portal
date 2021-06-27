from rest_framework import serializers
from .models import Student, Teacher, Batch

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    teacher_list = serializers.StringRelatedField(many=True)
    student_list = serializers.StringRelatedField(many=True)
    class Meta:
        model = Batch 
        fields = ['id', 'name', 'total_classes', 'completed_classes', 'teacher_list', 'student_list']