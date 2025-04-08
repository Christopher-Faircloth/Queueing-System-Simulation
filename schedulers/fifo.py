from collections import deque
from .base import Scheduler

class FIFOScheduler(Scheduler):
    def __init__(self):
        self.queue = deque()

    def add_job(self, job):
        self.queue.append(job)

    def get_next_job(self):
        return self.queue.popleft()

    def has_jobs(self):
        return len(self.queue) > 0
