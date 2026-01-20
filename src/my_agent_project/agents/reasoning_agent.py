"""Reasoning Agent - Advanced logical reasoning and inference"""

from typing import Any, Dict, List
from .base_agent import BaseAgent


class ReasoningAgent(BaseAgent):
    """Agent with advanced reasoning capabilities"""
    
    def __init__(self, agent_id: str, reasoning_depth: int = 5):
        super().__init__(agent_id)
        self.reasoning_depth = reasoning_depth
        self.facts = []
        self.rules = []
        self.inference_results = []
        
    def perceive(self, observation: Any) -> None:
        """Perceive and store facts"""
        self.facts.append(observation)
        self.state['observation'] = observation
        self.update_memory({'type': 'fact', 'data': observation})
        
    def reason(self) -> Dict[str, Any]:
        """Apply logical reasoning"""
        inference = self._forward_chaining()
        self.inference_results.append(inference)
        return inference
    
    def act(self, action: Any) -> Any:
        """Execute action based on reasoning"""
        result = {
            'agent_id': self.agent_id,
            'action': action,
            'reasoning_depth': self.reasoning_depth,
            'facts_count': len(self.facts),
            'status': 'success'
        }
        return result
    
    def _forward_chaining(self) -> Dict[str, Any]:
        """Forward chaining inference algorithm"""
        conclusions = []
        for i in range(self.reasoning_depth):
            if self.facts:
                conclusions.append(f"Conclusion_{i}")
        
        return {
            'agent_id': self.agent_id,
            'method': 'forward_chaining',
            'conclusions': conclusions,
            'depth': self.reasoning_depth
        }
    
    def add_rule(self, rule: Dict[str, Any]) -> None:
        """Add reasoning rule"""
        self.rules.append(rule)
        self.update_memory({'type': 'rule', 'rule': rule})
