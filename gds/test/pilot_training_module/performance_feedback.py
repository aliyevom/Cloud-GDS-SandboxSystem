import smtplib
import sqlite3
from email.mime.text import MIMEText
from datetime import datetime

class PerformanceFeedback:
    def __init__(self, db_path="feedback.db"):
        self.db_path = db_path
        self._setup_database()

    def _setup_database(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS feedback
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      pilot_id TEXT, 
                      feedback TEXT, 
                      timestamp TEXT)''')
        conn.commit()
        conn.close()

    def store_feedback(self, pilot_id, feedback):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO feedback (pilot_id, feedback, timestamp) VALUES (?, ?, ?)",
                  (pilot_id, feedback, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def send_feedback_email(self, pilot_id, feedback):
        msg = MIMEText(feedback)
        msg['Subject'] = 'Performance Feedback'
        msg['From'] = 'noreply@airline.com'
        msg['To'] = f'{pilot_id}@airline.com'

        try:
            with smtplib.SMTP('smtp.mailserver.com') as server:
                server.sendmail(msg['From'], [msg['To']], msg.as_string())
            print(f"Feedback email sent to {pilot_id}")
        except Exception as e:
            print(f"Failed to send feedback email: {e}")

    def process_feedback(self, pilot_id, feedback):
        print(f"Processing feedback for pilot {pilot_id}...")
        self.store_feedback(pilot_id, feedback)
        self.send_feedback_email(pilot_id, feedback)
        print("Feedback processed and stored successfully.")

if __name__ == "__main__":
    feedback_system = PerformanceFeedback()

    # Simulated feedback from training assessment
    feedback = "Your performance is satisfactory. Keep it up!"
    pilot_id = "Pilot123"

    feedback_system.process_feedback(pilot_id, feedback)
