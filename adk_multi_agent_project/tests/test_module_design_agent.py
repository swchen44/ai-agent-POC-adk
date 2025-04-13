from agents.module_design_agent import prompt
def test_prompt_loaded():
    assert "Module Design Agent" in prompt.prompt
