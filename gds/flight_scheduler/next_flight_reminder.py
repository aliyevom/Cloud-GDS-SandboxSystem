import smtplib
from email.mime.text import MIMEText
import logging
from flight_scheduler_pb2_grpc import FlightSchedulerStub
import grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NextFlightReminder:
    def __init__(self, scheduler_stub):
        self.scheduler_stub = scheduler_stub

    def send_reminder(self, pilot_email, flight_info):
        subject = f"Reminder: Upcoming Flight to {flight_info['destination']}"
        body = f"Dear Pilot, your flight {flight_info['flight_id']} is scheduled on {flight_info['scheduled_date']}. Please be prepared."
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "noreply@airline.com"
        msg['To'] = pilot_email

        try:
            with smtplib.SMTP('smtp.mailtrap.io', 587) as server:
                server.login("your_username", "your_password")
                server.sendmail("noreply@airline.com", [pilot_email], msg.as_string())
                logger.info(f"Reminder sent to {pilot_email} for flight {flight_info['flight_id']}.")
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")

    def check_and_send_reminders(self):
        # Example to fetch flights
        # This would actually involve fetching upcoming flights from the backend.
        flights = [
            {"flight_id": "FL123", "pilot_id": "Pilot123", "scheduled_date": "2024-09-15T10:00:00", "destination": "JFK"}
        ]
        for flight in flights:
            pilot_email = self.get_pilot_email(flight["pilot_id"])
            if pilot_email:
                self.send_reminder(pilot_email, flight)

    def get_pilot_email(self, pilot_id):
        # Sim
