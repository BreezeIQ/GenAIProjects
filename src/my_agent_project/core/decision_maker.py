"""Decision Maker module - Decision-making logic"""

from typing import Any, Dict, List, Optional


class DecisionMaker:
    """Decision-making system"""
    
    def __init__(self, decision_strategy: str = 'greedy'):
        self.decision_strategy = decision_strategy
        self.decisions_log = []
        self.preferences = {}
        
    def decide(self, options: List[Dict[str, Any]], context: Dict = None) -> Dict[str, Any]:
        """Make decision based on available options"""
        if self.decision_strategy == 'greedy':
            decision = self._greedy_decision(options)
        elif self.decision_strategy == 'utility':
            decision = self._utility_decision(options)
        else:
            decision = self._random_decision(options)
        
        self.decisions_log.append(decision)
        return decision
    
    def _greedy_decision(self, options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Greedy decision making"""
        if not options:
            return {'decision': None, 'strategy': 'greedy', 'reason': 'no_options'}
        
        best = max(options, key=lambda x: x.get('score', 0))
        return {
            'decision': best.get('action'),
            'strategy': 'greedy',
            'score': best.get('score'),
            'reason': 'maximum_score'
        }
    
    def _utility_decision(self, options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Utility-based decision making"""
        max_utility = -float('inf')
        best_option = None
        
        for option in options:
            utility = self._calculate_utility(option)
            if utility > max_utility:
                max_utility = utility
                best_option = option
        
        return {
            'decision': best_option.get('action') if best_option else None,
            'strategy': 'utility',
            'utility': max_utility,
            'reason': 'maximum_utility'
        }
    
    def _random_decision(self, options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Random decision making"""
        import random
        if not options:
            return {'decision': None, 'strategy': 'random', 'reason': 'no_options'}
        
        choice = random.choice(options)
        return {
            'decision': choice.get('action'),
            'strategy': 'random',
            'reason': 'random_selection'
        }
    
    def _calculate_utility(self, option: Dict[str, Any]) -> float:
        """Calculate utility of option"""
        weight_score = 0.7
        weight_probability = 0.3
        
        score = option.get('score', 0) * weight_score
        probability = option.get('probability', 0) * weight_probability
        
        return score + probability
    
    def set_preference(self, key: str, value: float) -> None:
        """Set preference for decision factor"""
        self.preferences[key] = value
    
    def get_decision_metrics(self) -> Dict[str, Any]:
        """Get decision-making metrics"""
        return {
            'total_decisions': len(self.decisions_log),
            'strategy': self.decision_strategy,
            'preferences': self.preferences
        }
