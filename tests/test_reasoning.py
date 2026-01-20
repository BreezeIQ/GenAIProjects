"""Test reasoning module"""

import unittest
from src.my_agent_project.core.reasoning import ForwardChainingEngine


class TestForwardChaining(unittest.TestCase):
    """Test forward chaining reasoning"""
    
    def setUp(self):
        self.engine = ForwardChainingEngine(max_iterations=10)
    
    def test_forward_chaining_simple(self):
        facts = ['A', 'B']
        rules = [
            {'conditions': ['A', 'B'], 'conclusion': 'C'},
        ]
        
        conclusions = self.engine.reason(facts, rules)
        self.assertIn('A', conclusions)


if __name__ == '__main__':
    unittest.main()
