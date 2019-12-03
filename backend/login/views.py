from django.contrib.auth.models import User
from rest_framework import viewsets
from login.serializers import UserSerializer, ClassesSerializer, StudentSerializer, DailyAttendanceSerializer
from login.models import Classes, Students, DailyAttendance


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ClassesView(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class DailyAttendanceViewSet(viewsets.ModelViewSet):
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer
