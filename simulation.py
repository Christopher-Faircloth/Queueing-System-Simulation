import numpy as np
import pandas as pd
from schedulers.fifo import FIFOScheduler  # Example, use other schedulers too
from job import Job

class Simulation:
    def __init__(self, scheduler, num_jobs=1000, arrival_rate=1.0):
        self.scheduler = scheduler
        self.num_jobs = num_jobs
        self.arrival_rate = arrival_rate
        self.jobs = []
        self.results = []

    def generate_jobs(self):
        arrival_times = np.cumsum(np.random.exponential(1/self.arrival_rate, self.num_jobs))
        service_times = np.random.exponential(scale=2.0, size=self.num_jobs)  # Adjust as needed
        self.jobs = [Job(i, arrival_times[i], service_times[i]) for i in range(self.num_jobs)]

    def run(self):
        self.generate_jobs()
        for job in self.jobs:
            self.scheduler.add_job(job)

        time = 0
        while self.scheduler.has_jobs():
            job = self.scheduler.get_next_job()
            job.start_time = max(time, job.arrival_time)
            job.finish_time = job.start_time + job.service_time
            time = job.finish_time
            self.results.append({
                "job_id": job.job_id,
                "arrival_time": job.arrival_time,
                "start_time": job.start_time,
                "finish_time": job.finish_time,
                "waiting_time": job.start_time - job.arrival_time
            })

    def analyze_results(self):
        df = pd.DataFrame(self.results)
        print(df.describe())  # Summary statistics
        df.to_csv("results.csv", index=False) 

# Example Usage
if __name__ == "__main__":
    sim = Simulation(FIFOScheduler(), num_jobs=1000, arrival_rate=0.5)
    sim.run()
    sim.analyze_results()
