import sys, os
BIN = os.path.expanduser("../../PySTUFF")
sys.path.append(BIN)


from PyECLOUD.buildup_simulation import BuildupSimulation

# Build the simulation object
sim = BuildupSimulation(extract_sey=False)
# Run the simulation 
sim.run()
