import unittest
from src.simulation import run_simulation

class TestSimulation(unittest.TestCase):
    def test_simulation_runs(self):
        # Ensure the simulation runs without errors
        try:
            run_simulation()
        except Exception as e:
            self.fail(f"Simulation failed with exception: {e}")
