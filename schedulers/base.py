from abc import ABC, abstractmethod

class Scheduler(ABC):
    @abstractmethod
    def add_job(self, job):
        pass

    @abstractmethod
    def get_next_job(self):
        pass

    @abstractmethod
    def has_jobs(self):
        pass
