"""Collaborative Agent - Multi-agent collaboration and communication"""

from typing import Any, Dict, List
from .base_agent import BaseAgent


class CollaborativeAgent(BaseAgent):
    """Agent that collaborates with other agents"""
    
    def __init__(self, agent_id: str, team_size: int = 5):
        super().__init__(agent_id)
        self.team_size = team_size
        self.team_members = []
        self.shared_knowledge = {}
        self.communication_log = []
        
    def perceive(self, observation: Any) -> None:
        """Perceive environment"""
        self.state['observation'] = observation
        self.update_memory({'type': 'observation', 'data': observation})
        self._broadcast_to_team(observation)
        
    def reason(self) -> Dict[str, Any]:
        """Collaborative reasoning"""
        decision = {
            'agent_id': self.agent_id,
            'team_members': len(self.team_members),
            'shared_knowledge_items': len(self.shared_knowledge),
            'action': 'collaborative_action'
        }
        return decision
    
    def act(self, action: Any) -> Any:
        """Execute collaborative action"""
        result = {
            'agent_id': self.agent_id,
            'action': action,
            'collaboration_level': len(self.team_members) / max(1, self.team_size),
            'status': 'success'
        }
        return result
    
    def add_team_member(self, member_id: str) -> None:
        """Add team member"""
        if member_id not in self.team_members:
            self.team_members.append(member_id)
            self.update_memory({'type': 'team_member_added', 'member_id': member_id})
    
    def _broadcast_to_team(self, message: Any) -> None:
        """Broadcast message to team"""
        comm = {
            'from': self.agent_id,
            'message': message,
            'timestamp': len(self.communication_log)
        }
        self.communication_log.append(comm)
    
    def get_team_status(self) -> Dict[str, Any]:
        """Get team collaboration status"""
        return {
            'agent_id': self.agent_id,
            'team_size': len(self.team_members),
            'communication_count': len(self.communication_log),
            'shared_knowledge_items': len(self.shared_knowledge)
        }
