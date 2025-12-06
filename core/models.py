from django.db import models

class Contact(models.Model):
    TIME_CHOICES = [
        ('morning', 'Morning (9am - 12pm)'),
        ('afternoon', 'Afternoon (12pm - 5pm)'),
        ('evening', 'Evening (5pm - 8pm)'),
    ]

    PROJECT_CHOICES = [
        ('exterior', 'Exterior painting'),
        ('interior', 'Interior painting'),
        ('both', 'Both interior & exterior'),
        ('commercial', 'Commercial project'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    preferred_time = models.CharField(max_length=20, choices=TIME_CHOICES, blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_CHOICES, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
