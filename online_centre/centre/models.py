from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.URLField(null=True)  
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
   
    title = models.CharField(max_length=300, null=True)
    description = models.TextField()
    image = models.URLField(default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course_id.title} at {self.enrolled_at}"
    