from google.adk.agents import LlmAgent
from .prompt import prompt

agent = LlmAgent(
    name="SystemDesigner",
    instruction=prompt,
    model="text-bison-001",
    output_key="system_design"
)