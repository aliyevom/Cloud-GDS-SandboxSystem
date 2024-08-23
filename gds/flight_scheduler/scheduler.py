import grpc
from datetime import datetime
import logging
import flight_scheduler_pb2
import flight_scheduler_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlightSchedulerClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = flight_scheduler_pb2_grpc.FlightSchedulerStub(self.channel)

    def schedule_flight(self, pilot_id, aircraft_id, destination, flight_date):
        try:
            request = flight_scheduler_pb2.ScheduleFlightRequest(
                pilot_id=pilot_id,
                aircraft_id=aircraft_id,
                destination=destination,
                flight_date=flight_date
            )
            response = self.stub.ScheduleFlight(request)
            logger.info(f"Flight scheduled successfully: {response.confirmation_message}")
            return response
        except grpc.RpcError as e:
            logger.error(f"gRPC error: {e.code()} - {e.details()}")
            return None

if __name__ == "__main__":
    scheduler = FlightSchedulerClient()
    flight_date = datetime.now().isoformat()
    scheduler.schedule_flight("Pilot123", "A320", "JFK", flight_date)
