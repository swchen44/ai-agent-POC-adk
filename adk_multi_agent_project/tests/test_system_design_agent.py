from agents.system_design_agent import prompt
def test_prompt_loaded():
    assert "System Design Agent" in prompt.prompt
