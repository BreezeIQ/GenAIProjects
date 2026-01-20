"""Multi-Agent Example"""

from my_agent_project.agents.collaborative_agent import CollaborativeAgent


def main():
    """Run multi-agent example"""
    
    agents = [
        CollaborativeAgent("agent_001", team_size=3),
        CollaborativeAgent("agent_002", team_size=3),
    ]
    
    for agent in agents:
        for other in agents:
            if agent.agent_id != other.agent_id:
                agent.add_team_member(other.agent_id)
    
    print("Multi-Agent Collaboration Demo")
    
    for agent in agents:
        agent.perceive("Team observation")
        decision = agent.reason()
        agent.act(decision['action'])
        status = agent.get_team_status()
        print(f"{agent.agent_id}: Team Size={status['team_size']}")


if __name__ == "__main__":
    main()
