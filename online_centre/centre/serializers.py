from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import UserProfile, Course, Lesson, Enrollment, Category

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        def validate(self, attrs):
            ism_familiya = attrs['full_name']
            if ism_familiya:
                for i in ism_familiya:
                    if i.isdigit():
                        raise ValidationError("Ism familiyada raqam bo'lishi mumkinmas")
            return attrs
        
        def validate_age(self, attrs):
            if attrs['age'] < 0:
                raise ValidationError("Yosh manfiy bo'lishi mumkin emas")
            return attrs


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        def validate(self, attrs):
            if attrs['price'] < 0:
                raise ValidationError("Narx manfiy bo'lishi mumkin emas")
            return attrs

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        def validate(self, attrs):
            if attrs['duration'] < 0:
                raise ValidationError("Davomiylik manfiy bo'lishi mumkin emas")
            return attrs


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student', 'course_id']
