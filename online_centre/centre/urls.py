from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, CourseViewSet, LessonViewSet, EnrollmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserProfileViewSet) 
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'enrollments', EnrollmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]