import itertools
import multiprocessing
import os
import subprocess

# Define execution parameters
num_processes = 4
executable = os.path.join(os.getcwd(), "dummy.sh")

# Define the parameter space
lambdas = [1]
mus = [1]
resistances = [1e-2, 1, 1e2]
alphas = [1]
storages = [0]
timesteps = [1]
relaxations = [0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.175, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]

# Define the list of parameters. The order given here defines the
# order in which they appear as command line arguments to above
# executable.
parameters = [lambdas, mus, resistances, alphas, storages, timesteps, relaxations]


# The function that executes a single run. This can also handle
# creation of a suitable working directory, log redirection,
# setting of environment variables etc.
def run_simulation(args):
    # Actually run with subprocess
    result = subprocess.run(
        (executable,) + tuple(str(x) for x in args), capture_output=False
    )

    # Produce an error if the return code was not 0
    if result.returncode != 0:
        raise RuntimeError(f"Simulation with parameters {args} failed")


# Start the Jobs within a process pool - only num_processes
# processes are active at the same time
with multiprocessing.Pool(num_processes) as p:
    # Build the product space of the specifed parameters
    for args in itertools.product(*parameters):
        p.apply_async(run_simulation, [args])

    # Make sure that the execution of this Python script
    # blocks until all jobs have been processed
    p.close()
    p.join()
