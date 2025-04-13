from google.adk.agents import LlmAgent
from .prompt import prompt

agent = LlmAgent(
    name="RequirementAnalyzer",
    instruction=prompt,
    model="text-bison-001",
    output_key="requirements"
)