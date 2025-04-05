from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    username = models.CharField(max_length=150, unique=True, null=True)
    password = models.CharField(max_length=128, null=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.URLField(null=True)  
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"


class Course(models.Model):
    CATEGORY_CHOICES = (
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('business', 'Business'),
    )

    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='programming')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 


    def __str__(self):
        return f"{self.category} ({self.description})"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    topic = models.CharField(max_length=100, default="")
    video = models.URLField(default="")

    def __str__(self):
        return f"{self.course} - {self.topic}"


class Enrollment(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.lesson.course} at {self.enrolled_at}"
    