from google.adk.agents import LlmAgent
from .prompt import prompt

agent = LlmAgent(
    name="ModuleDesigner",
    instruction=prompt,
    model="text-bison-001",
    output_key="module_plan"
)