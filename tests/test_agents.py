"""Test agents module"""

import unittest
from src.my_agent_project.agents.autonomous_agent import AutonomousAgent


class TestAutonomousAgent(unittest.TestCase):
    """Test autonomous agent"""
    
    def setUp(self):
        self.agent = AutonomousAgent("autonomous_1", independence_level=0.9)
    
    def test_autonomy_level(self):
        self.assertEqual(self.agent.independence_level, 0.9)
    
    def test_goal_setting(self):
        self.agent.set_goal("test_goal")
        self.assertEqual(self.agent.goal, "test_goal")


if __name__ == '__main__':
    unittest.main()
