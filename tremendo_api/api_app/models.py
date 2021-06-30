from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.BigIntegerField(blank=True, default=0)
    address = models.TextField(blank=True)
    # batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="teacher_list")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone_number}, {self.address}"

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_OPTIONS = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
        )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=True)
    address = models.TextField(blank=True)
    # batch = models.ManyToManyField(Batch, related_name="student_list")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.gender}, {self.address}"

class Batch(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_list")
    students = models.ManyToManyField(Student, related_name="student_list")
    total_classes = models.IntegerField(default=10) 
    completed_classes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.total_classes}, {self.completed_classes}, {self.teacher}, {self.students}"

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
