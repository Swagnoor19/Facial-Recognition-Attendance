from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

fs = "students/"

class Classes(models.Model):
    courseId = models.IntegerField()
    courseName = models.TextField()
    meetingSchedule = models.TextField()
    username  =  models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # otherwise we get "Studentss in admin"
        verbose_name_plural = "Classes"

    def __str__(self):
        return '%s' %(self.courseId)

class Students(models.Model):
    courseId = models.ForeignKey(Classes, on_delete=models.CASCADE)
    studentName  = models.TextField()
    school_id = models.CharField(max_length = 200)
    attendence = models.CharField(max_length = 800)
    studentPicture = models.ImageField(upload_to = fs ,blank=False, null=False, default=1)

    class Meta:
        # otherwise we get "Studentss in admin"
        verbose_name_plural = "Students"

    def __str__(self):
        return '%s' %(self.courseId)
        
