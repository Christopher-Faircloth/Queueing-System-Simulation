from simulation import Simulation
from schedulers.fifo import FIFOScheduler

if __name__ == "__main__":
    scheduler = FIFOScheduler()
    sim = Simulation(scheduler, num_jobs=1000, arrival_rate=0.5)
    sim.run()
    sim.analyze_results()
