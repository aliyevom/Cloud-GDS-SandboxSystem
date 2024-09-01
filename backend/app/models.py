# app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    # Adding fields for different roles like pilots, instructors, etc.
    is_pilot = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    capacity = models.IntegerField()
    simulator_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Pilot(models.Model):
    EXPERIENCE_LEVELS = [
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('captain', 'Captain'),
    ]

    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    rating = models.CharField(max_length=10)
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_LEVELS)
    assigned_aircraft = models.ManyToManyField(Aircraft, related_name='pilots')

    def __str__(self):
        return self.name

    def available_for_training(self):
        current_sessions = self.trainingsessions.filter(status='in_progress')
        return current_sessions.count() == 0

class TrainingSession(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    session_id = models.CharField(max_length=20, unique=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='trainingsessions')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='trainingsessions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    instructor_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.session_id

    def complete_session(self):
        self.status = 'completed'
        self.end_time = timezone.now()
        self.save()

class Evaluation(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(Pilot, on_delete=models.SET_NULL, null=True, related_name='evaluations_given')
    score = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f'Evaluation for {self.session.session_id} by {self.evaluator.name}'
