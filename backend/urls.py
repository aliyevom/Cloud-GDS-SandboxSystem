# urls.py

from django.contrib import admin
from django.urls import path
from app.views import TrainingSessionListView, PilotDetailView, EvaluationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sessions/', TrainingSessionListView.as_view(), name='training-session-list'),
    path('pilots/<int:pilot_id>/', PilotDetailView.as_view(), name='pilot-detail'),
    path('evaluations/', EvaluationView.as_view(), name='evaluation'),
]
