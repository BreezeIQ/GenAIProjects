from typing import Any
from my_agent_project.agents.base_agent import BaseAgent

class MyFirstAgent(BaseAgent):
    def perceive(self, observation: Any) -> None:
        """Perceive environment"""
        self.state['observation'] = observation
        self.update_memory({'type': 'observation', 'data': observation})

    def reason(self) -> Any:
        """Make decision"""
        observation = self.state.get('observation', 'unknown')
        return f"Decision based on {observation}"

    def act(self, decision: Any) -> Any:
        """Execute action"""
        print(f"Action taken: {decision}")
        return {'status': 'success', 'action': decision}
