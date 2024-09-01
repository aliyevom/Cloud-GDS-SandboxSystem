# app/signals.py

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import TrainingSession, Evaluation

@receiver(pre_save, sender=TrainingSession)
def update_training_session_status(sender, instance, **kwargs):
    if instance.end_time and instance.end_time < timezone.now():
        instance.status = 'completed'

@receiver(post_save, sender=Evaluation)
def update_pilot_rating(sender, instance, created, **kwargs):
    if created:
        pilot = instance.session.pilot
        # Adjust pilot's rating or other fields based on evaluations
        pilot.rating = calculate_new_rating(pilot)
        pilot.save()

def calculate_new_rating(pilot):
    # A placeholder function to calculate pilot's rating based on evaluations
    evaluations = Evaluation.objects.filter(session__pilot=pilot)
    total_score = sum([eval.score for eval in evaluations])
    return total_score / len(evaluations)
