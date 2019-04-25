import rps.robotarium as robotarium
import rps.utilities.graph as graph
import rps.utilities.transformations as transformations
from rps.utilities.barrier_certificates import *
from rps.utilities.controllers import *
import numpy as np

# How many robots we want to use in the simulation
N = 1
# Instantiate the Robotarium object with these parameters
r = robotarium.Robotarium(number_of_agents=N, show_figure=True, save_data=True, update_time=0.1)

# How many iterations do we want (about 165 seconds)
iterations = 5000

# Define the desired path
R = 1
b = 1
n = 3

