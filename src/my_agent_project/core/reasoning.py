"""Reasoning module - Core reasoning engine"""

from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod


class ReasoningEngine(ABC):
    """Abstract reasoning engine"""
    
    @abstractmethod
    def reason(self, facts: List[Any], rules: List[Dict]) -> List[Any]:
        """Apply reasoning to derive conclusions"""
        pass


class ForwardChainingEngine(ReasoningEngine):
    """Forward chaining reasoning engine"""
    
    def __init__(self, max_iterations: int = 100):
        self.max_iterations = max_iterations
        self.conclusions = []
        
    def reason(self, facts: List[Any], rules: List[Dict]) -> List[Any]:
        """Forward chaining algorithm"""
        known_facts = set(facts)
        
        for _ in range(self.max_iterations):
            new_facts = set()
            for rule in rules:
                if self._check_conditions(rule, known_facts):
                    conclusion = rule.get('conclusion')
                    if conclusion and conclusion not in known_facts:
                        new_facts.add(conclusion)
            
            if not new_facts:
                break
            known_facts.update(new_facts)
        
        self.conclusions = list(known_facts)
        return self.conclusions
    
    def _check_conditions(self, rule: Dict, facts: set) -> bool:
        """Check if rule conditions are met"""
        conditions = rule.get('conditions', [])
        return all(cond in facts for cond in conditions)
