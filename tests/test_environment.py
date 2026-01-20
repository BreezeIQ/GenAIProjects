"""Test environment module"""

import unittest
from src.my_agent_project.environment.simulator import EnvironmentSimulator


class TestEnvironmentSimulator(unittest.TestCase):
    """Test environment simulator"""
    
    def setUp(self):
        self.env = EnvironmentSimulator("test_env", size=(50, 50))
    
    def test_environment_initialization(self):
        self.assertEqual(self.env.env_id, "test_env")
        self.assertEqual(self.env.size, (50, 50))
    
    def test_reset(self):
        self.env.add_agent("agent_1")
        state = self.env.reset()
        self.assertEqual(state['agents'], 1)
        self.assertEqual(self.env.timestep, 0)


if __name__ == '__main__':
    unittest.main()
