# app/tests.py

from django.test import TestCase
from django.utils import timezone
from .models import Aircraft, Pilot, TrainingSession, Evaluation

class PilotModelTest(TestCase):

    def setUp(self):
        self.aircraft = Aircraft.objects.create(name="Boeing 747", manufacturer="Boeing", capacity=416, simulator_available=True)
        self.pilot = Pilot.objects.create(name="John Doe", license_number="XYZ456", rating="A", experience_level="junior")

    def test_pilot_availability(self):
        session = TrainingSession.objects.create(
            session_id="TS123",
            pilot=self.pilot,
            aircraft=self.aircraft,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=2),
            status="in_progress"
        )
        self.assertFalse(self.pilot.available_for_training())

class TrainingSessionTest(TestCase):

    def setUp(self):
        self.aircraft = Aircraft.objects.create(name="Boeing 747", manufacturer="Boeing", capacity=416, simulator_available=True)
        self.pilot = Pilot.objects.create(name="Jane Smith", license_number="ABC123", rating="B", experience_level="senior")
        self.session = TrainingSession.objects.create(
            session_id="TS456",
            pilot=self.pilot,
            aircraft=self.aircraft,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=3),
            status="scheduled"
        )

    def test_complete_session(self):
        self.session.complete_session()
        self.assertEqual(self.session.status, "completed")

class EvaluationTest(TestCase):

    def setUp(self):
        self.aircraft = Aircraft.objects.create(name="Boeing 737", manufacturer="Boeing", capacity=200, simulator_available=True)
        self.pilot = Pilot.objects.create(name="John Doe", license_number="XYZ456", rating="A", experience_level="junior")
        self.instructor = Pilot.objects.create(name="Jane Smith", license_number="ABC123", rating="B", experience_level="senior")
        self.session = TrainingSession.objects.create(
            session_id="TS789",
            pilot=self.pilot,
            aircraft=self.aircraft,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=3),
            status="completed"
        )
        self.evaluation = Evaluation.objects.create(
            session=self.session,
            evaluator=self.instructor,
            score=85,
            remarks="Good job, needs improvement in landing technique."
        )

    def test_evaluation_creation(self):
        self.assertEqual(self.evaluation.score, 85)
        self.assertEqual(self.evaluation.evaluator, self.instructor)
