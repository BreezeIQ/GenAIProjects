"""Base Environment module"""

from typing import Any, Dict, List, Tuple
from abc import ABC, abstractmethod


class BaseEnvironment(ABC):
    """Abstract base environment class"""
    
    def __init__(self, env_id: str, size: Tuple[int, int] = (100, 100)):
        self.env_id = env_id
        self.size = size
        self.agents = []
        self.state = {}
        self.timestep = 0
        
    @abstractmethod
    def reset(self) -> Dict[str, Any]:
        """Reset environment"""
        pass
    
    @abstractmethod
    def step(self, actions: Dict[str, Any]) -> Tuple[Dict, Dict, bool]:
        """Execute environment step"""
        pass
    
    def add_agent(self, agent_id: str) -> None:
        """Add agent to environment"""
        if agent_id not in self.agents:
            self.agents.append(agent_id)
    
    def remove_agent(self, agent_id: str) -> None:
        """Remove agent from environment"""
        if agent_id in self.agents:
            self.agents.remove(agent_id)
    
    def get_state(self) -> Dict[str, Any]:
        """Get environment state"""
        return {
            'env_id': self.env_id,
            'timestep': self.timestep,
            'agents': len(self.agents),
            'size': self.size
        }
