# My AI Project

Comprehensive AI Agent Project with advanced reasoning, learning, and collaboration capabilities.

## Overview

This project provides a complete framework for developing intelligent agents with multiple agent types and core components.

## Project Structure

```tree
my_aiproject/
├── config/                          # Configuration files
│   ├── agent_config.yml            # Agent configurations
│   ├── system_config.yml           # System settings
│   ├── environment_config.yml      # Environment parameters
│   └── logging_config.yml          # Logging configuration
│
├── src/my_agent_project/
│   ├── agents/                      # Agent implementations
│   │   ├── base_agent.py           # Base agent
│   │   ├── my_first_agent.py       # Original agent
│   │   ├── autonomous_agent.py     # Autonomous agents
│   │   ├── learning_agent.py       # Learning agents
│   │   ├── reasoning_agent.py      # Reasoning agents
│   │   └── collaborative_agent.py  # Collaborative agents
│   │
│   ├── core/                        # Core components
│   │   ├── memory.py               # Memory management
│   │   ├── reasoning.py            # Reasoning engines
│   │   ├── learning.py             # Learning algorithms
│   │   ├── decision_maker.py       # Decision making
│   │   └── executor.py             # Task execution
│   │
│   ├── environment/                 # Environment system
│   │   ├── base_env.py             # Base environment
│   │   └── simulator.py            # Simulator
│   │
│   ├── utils/                       # Utilities
│   │   ├── logger.py               # Logging
│   │   ├── metrics.py              # Metrics
│   │   ├── visualizer.py           # Visualization
│   │   └── validator.py            # Validation
│   │
│   └── main.py                      # Entry point
│
├── data/                            # Data directory
│   ├── memory/, knowledge_base/, training/, logs/, checkpoints/
│
├── tests/                           # Test suite
├── examples/                        # Examples
├── notebooks/                       # Notebooks
├── pyproject.toml                   # Project config
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

## Key Components

### Agents

- **BaseAgent**: Foundation for all agents
- **MyFirstAgent**: Original simple agent
- **AutonomousAgent**: Independent decision-making
- **LearningAgent**: Learn from experience
- **ReasoningAgent**: Logical inference
- **CollaborativeAgent**: Multi-agent coordination

### Core Systems

- **Memory**: Agent memory management
- **Reasoning**: Forward chaining engines
- **Learning**: Training algorithms
- **DecisionMaker**: Utility-based decisions
- **Executor**: Task execution

### Environment

- **BaseEnvironment**: Abstract environment
- **EnvironmentSimulator**: Simulation

## Getting Started

```bash
# Run main agent
uv run my-agent

# Run tests
pytest tests/

# Run examples
python examples/single_agent.py
python examples/multi_agent.py
```


## Installation

```bash
pip install -r requirements.txt
```

## License

MIT License
