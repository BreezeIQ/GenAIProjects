"""Single Agent Example"""

from my_agent_project.agents.autonomous_agent import AutonomousAgent
from my_agent_project.environment.simulator import EnvironmentSimulator


def main():
    """Run single agent example"""
    
    agent = AutonomousAgent("agent_001", independence_level=0.8)
    agent.set_goal("Complete mission")
    
    env = EnvironmentSimulator("simple_env")
    env.add_agent(agent.agent_id)
    env.reset()
    
    print(f"Single Agent Simulation: {agent.agent_id}")
    
    for step in range(5):
        agent.perceive(f"Observation at step {step}")
        decision = agent.reason()
        result = agent.act(decision['action'])
        print(f"Step {step}: {result['status']}")


if __name__ == "__main__":
    main()
