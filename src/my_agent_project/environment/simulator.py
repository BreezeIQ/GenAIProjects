"""Environment Simulator module"""

from typing import Any, Dict, Tuple
from .base_env import BaseEnvironment


class EnvironmentSimulator(BaseEnvironment):
    """Simulated environment for agents"""
    
    def __init__(self, env_id: str, size: Tuple[int, int] = (100, 100), timestep_duration: float = 0.1):
        super().__init__(env_id, size)
        self.timestep_duration = timestep_duration
        self.resources = []
        self.obstacles = []
        self.episode_rewards = {}
        
    def reset(self) -> Dict[str, Any]:
        """Reset environment to initial state"""
        self.timestep = 0
        self.state = {
            'agents': len(self.agents),
            'resources': len(self.resources),
            'obstacles': len(self.obstacles)
        }
        self.episode_rewards = dict.fromkeys(self.agents, 0)
        return self.state
    
    def step(self, actions: Dict[str, Any]) -> Tuple[Dict, Dict, bool]:
        """Execute one simulation step"""
        self.timestep += 1
        
        observations = {}
        rewards = {}
        
        for agent_id, action in actions.items():
            observation = self._execute_action(agent_id, action)
            reward = self._calculate_reward(agent_id, observation)
            
            observations[agent_id] = observation
            rewards[agent_id] = reward
            self.episode_rewards[agent_id] += reward
        
        done = self.timestep >= 1000
        
        return observations, rewards, done
    
    def _execute_action(self, agent_id: str, action: Any) -> Dict[str, Any]:
        """Execute agent action in environment"""
        return {
            'agent_id': agent_id,
            'action': action,
            'timestep': self.timestep,
            'status': 'executed'
        }
    
    def _calculate_reward(self, _agent_id: str, observation: Dict) -> float:
        """Calculate reward for agent"""
        return 0.1 if observation['status'] == 'executed' else -0.1
    
    def add_resource(self, resource: Dict) -> None:
        """Add resource to environment"""
        self.resources.append(resource)
    
    def add_obstacle(self, obstacle: Dict) -> None:
        """Add obstacle to environment"""
        self.obstacles.append(obstacle)
    
    def get_episode_rewards(self) -> Dict[str, float]:
        """Get cumulative episode rewards"""
        return self.episode_rewards
