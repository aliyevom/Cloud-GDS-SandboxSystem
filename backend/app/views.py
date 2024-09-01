# app/views.py

from django.http import JsonResponse
from django.views import View
from .models import TrainingSession, Pilot, Evaluation

class TrainingSessionListView(View):
    def get(self, request):
        sessions = TrainingSession.objects.select_related('pilot', 'aircraft').all()
        session_data = [
            {
                "session_id": session.session_id,
                "pilot": session.pilot.name,
                "aircraft": session.aircraft.name,
                "status": session.status,
                "start_time": session.start_time,
                "end_time": session.end_time,
                "instructor_notes": session.instructor_notes,
            }
            for session in sessions
        ]
        return JsonResponse(session_data, safe=False)

class PilotDetailView(View):
    def get(self, request, pilot_id):
        pilot = Pilot.objects.prefetch_related('assigned_aircraft', 'trainingsessions').get(pk=pilot_id)
        pilot_data = {
            "name": pilot.name,
            "license_number": pilot.license_number,
            "rating": pilot.rating,
            "experience_level": pilot.experience_level,
            "assigned_aircraft": [aircraft.name for aircraft in pilot.assigned_aircraft.all()],
            "available_for_training": pilot.available_for_training(),
        }
        return JsonResponse(pilot_data)

class EvaluationView(View):
    def post(self, request):
        # Assume request contains JSON with session_id, evaluator_id, score, and remarks
        data = json.loads(request.body)
        session = TrainingSession.objects.get(session_id=data['session_id'])
        evaluator = Pilot.objects.get(pk=data['evaluator_id'])
        evaluation = Evaluation.objects.create(
            session=session,
            evaluator=evaluator,
            score=data['score'],
            remarks=data['remarks']
        )
        return JsonResponse({"message": "Evaluation submitted successfully", "evaluation_id": evaluation.id})
