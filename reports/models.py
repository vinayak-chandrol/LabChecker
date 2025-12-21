from django.db import models

# Create your models here.

class StudentData(models.Model):
    student_name=models.CharField(max_length=20)
    lab_name=models.CharField(max_length=100)
    lab_file=models.FileField(upload_to='lab_reports/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
