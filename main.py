from simulation import Simulation
from schedulers.fifo import FIFOScheduler

if __name__ == "__main__":
    scheduler = FIFOScheduler()
    sim = Simulation(scheduler, num_jobs=100, arrival_rate=.5, service_rate=1)
    sim.run()
    sim.analyze_results()
