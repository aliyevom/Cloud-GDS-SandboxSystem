# app/admin.py

from django.contrib import admin
from .models import Aircraft, Pilot, TrainingSession, Evaluation

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'capacity', 'simulator_available')
    search_fields = ('name', 'manufacturer')

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'rating', 'experience_level')
    search_fields = ('name', 'license_number')

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'pilot', 'aircraft', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'aircraft')
    search_fields = ('session_id', 'pilot__name', 'aircraft__name')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('session', 'evaluator', 'score', 'remarks')
    list_filter = ('score',)
    search_fields = ('session__session_id', 'evaluator__name')
