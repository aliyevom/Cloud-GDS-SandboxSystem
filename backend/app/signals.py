from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import TrainingSession, Evaluation

@receiver(pre_save, sender=TrainingSession)
def update_training_session_status(sender, instance, **kwargs):
    if instance.end_time and instance.end_time < timezone.now():
        instance.status = 'completed'

@receiver(post_save, sender=Evaluation)
def update_pilot_rating(sender, instance, created, **kwargs):
    if created:
        pilot = instance.session.pilot
        pilot.rating = calculate_new_rating(pilot)
        pilot.save()

def calculate_new_rating(pilot):
    evaluations = Evaluation.objects.filter(session__pilot=pilot)
    total_score = sum([eval.score for eval in evaluations])
    return total_score / len(evaluations) if evaluations else 0

@receiver(post_save, sender=TrainingSession)
def handle_training_session_completion(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.end_time < timezone.now():
        update_user_status(instance.user)

def update_user_status(user):
    # Implement user status update logic here
    pass

@receiver(post_save, sender=Evaluation)
def send_evaluation_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"New Evaluation for Training Session {instance.session.id}"
        message = f"Evaluation details: {instance.details}"
        recipient_list = [instance.session.pilot.email]
        send_mail(subject, message, 'from@example.com', recipient_list)
