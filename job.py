class Job:
    def __init__(self, job_id, arrival_time, service_time):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.remaining_time = service_time  # Needed for SRTF
        self.start_time = None
        self.finish_time = None

    def __repr__(self):
        return f"Job({self.job_id}, Arrival: {self.arrival_time}, Service: {self.service_time})"
