# complaintmgmtsys/models.py
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver  # Import settings to use AUTH_USER_MODEL

class Complaints(models.Model):
    complaint_number = models.CharField(max_length=100, unique=True)
    userregid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    status = models.CharField(max_length=20, choices=[
        ('0', 'Not Processed Yet'),
        ('Inprocess', 'In Process'),
        ('Closed', 'Closed'),
    ])
    complaintdate_at = models.DateTimeField(auto_now_add=True)
    noc = models.CharField(max_length=255)  # Nature of Complaint
    complaindetails = models.TextField()  # Details of the complaint
    compfile = models.FileField(upload_to='complaint_files/', blank=True, null=True)  # Optional file upload
    feedback = models.TextField(blank=True, null=True)  # Field to store feedback
    rating = models.IntegerField(blank=True, null=True)
      
    def __str__(self):
        return self.complaint_number
