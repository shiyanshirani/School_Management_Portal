from django.db import models

class Batch(models.Model):
    name = models.CharField(max_length=100)
    total_classes = models.IntegerField(default=10) 
    completed_classes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, {self.total_classes}, {self.completed_classes}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.BigIntegerField(blank=True, default=0)
    address = models.TextField(blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="teacher_list")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone_number}, {self.address}, {self.batch}"

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
    batch = models.ManyToManyField(Batch, related_name="student_list")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.gender}, {self.address}, {self.batch}"
