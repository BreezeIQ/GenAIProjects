"""Learning module - Learning algorithms and models"""

from typing import Any, Dict, List, Optional
import random


class LearningModel:
    """Base learning model"""
    
    def __init__(self, learning_rate: float = 0.01, discount_factor: float = 0.9):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.weights = {}
        self.training_history = []
        
    def train(self, state: Any, action: Any, reward: float, next_state: Any) -> None:
        """Train the model"""
        delta = reward + self.discount_factor * self._get_value(next_state)
        delta -= self._get_value(state)
        
        state_key = str(state)
        if state_key not in self.weights:
            self.weights[state_key] = 0
        
        self.weights[state_key] += self.learning_rate * delta
        self.training_history.append({
            'state': state,
            'action': action,
            'reward': reward,
            'delta': delta
        })
    
    def predict(self, state: Any) -> float:
        """Predict value for state"""
        return self._get_value(state)
    
    def _get_value(self, state: Any) -> float:
        """Get value for state"""
        return self.weights.get(str(state), 0.0)
    
    def get_training_metrics(self) -> Dict[str, Any]:
        """Get training metrics"""
        if not self.training_history:
            return {}
        
        rewards = [h['reward'] for h in self.training_history]
        deltas = [h['delta'] for h in self.training_history]
        
        return {
            'total_episodes': len(self.training_history),
            'average_reward': sum(rewards) / len(rewards),
            'average_delta': sum(deltas) / len(deltas),
            'max_reward': max(rewards),
            'min_reward': min(rewards)
        }
