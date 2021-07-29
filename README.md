# python-run-parallel

This is a small Python script that traverses a combinatorial parameter space and executes a given executable with each parameter set. Execution is controlled through a process pool that limits the number of concurrent processes.

## How to run it

After cloning the repository do:

```
python run_parallel.py
```

This will execute the dummy script (which echoes the parameters and sleeps a second) with 4 processes.
