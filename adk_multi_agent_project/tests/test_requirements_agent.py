from agents.requirement_agent import prompt
def test_prompt_loaded():
    assert "Requirement Analysis Agent" in prompt.prompt
