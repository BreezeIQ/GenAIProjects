from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseAgent(ABC):
    """Abstract base class for all agents"""
    
    def __init__(self, agent_id: str, memory_size: int = 1000):
        self.agent_id = agent_id
        self.memory = []
        self.memory_size = memory_size
        self.state = {}
        
    @abstractmethod
    def perceive(self, observation: Any) -> None:
        """Process environment observation"""
        pass
    
    @abstractmethod
    def reason(self) -> Any:
        """Reasoning and decision-making logic"""
        pass
    
    @abstractmethod
    def act(self, action: Any) -> Any:
        """Execute action in environment"""
        pass
    
    def update_memory(self, data: Dict[str, Any]) -> None:
        """Update agent memory"""
        if len(self.memory) >= self.memory_size:
            self.memory.pop(0)
        self.memory.append(data)
        
    def get_memory(self) -> list:
        """Retrieve agent memory"""
        return self.memory
    
    def reset(self) -> None:
        """Reset agent state"""
        self.memory.clear()
        self.state.clear()
