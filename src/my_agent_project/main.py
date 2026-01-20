from my_agent_project.agents.my_first_agent import MyFirstAgent

def main():
    agent = MyFirstAgent(agent_id="agent_1")

    agent.perceive("Hello world")
    decision = agent.reason()
    agent.act(decision)

if __name__ == "__main__":
    main()

