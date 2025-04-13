from google.adk.agents import SequentialAgent
from agents.requirement_agent.agent import agent as requirement_agent
from agents.system_design_agent.agent import agent as system_agent
from agents.module_design_agent.agent import agent as module_agent

agent = SequentialAgent(
    name="DesignPipeline",
    sub_agents=[
        requirement_agent,
        system_agent,
        module_agent
    ]
)
