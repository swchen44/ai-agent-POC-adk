# ADK Multi-Agent POC — Design Overview

This document provides an in-depth explanation of the design, goals, comparisons, limitations, and future roadmap of the ADK multi-agent system. It supplements the technical README with a broader architectural and conceptual view.

---

## 🎯 Project Purpose

- Enable **multi-step software co-design** using LLM agents, modeled on the V-Model development lifecycle.
- Leverage **separation of concerns** through modular agents: requirements analysis, system design, and module decomposition.
- Provide plug-and-play support for **multiple LLM backends** via LiteLLM: Google PaLM, OpenAI, Ollama.
- Offer both **CLI and Web UI** interfaces through Google ADK.

---

## 🧱 System Architecture

```mermaid
flowchart TD
    A[User Input]
    A --> R[Requirement Analysis Agent]
    R --> S[System Design Agent]
    S --> M[Module Design Agent]
    M --> O[Markdown Design + Code Snippets]
```

Each agent receives shared `state`, enriching or transforming it:
- ✅ `RequirementAnalyzer` → produces `state['requirements']`
- ✅ `SystemDesigner` → produces `state['system_design']`
- ✅ `ModuleDesigner` → produces `state['module_plan']`

---

## ⚖️ Comparison: ADK vs Traditional Prompt Chains

| Feature                        | ADK Multi-Agent Workflow     | Manual Prompt Chains        |
|-------------------------------|-------------------------------|------------------------------|
| Memory Sharing                | ✅ via `state` object         | ❌ manual copy-paste         |
| Modularity                    | ✅ agent-per-role             | ❌ mixed logic                |
| Prompt Customization          | ✅ each agent loads from file | ❌ inline/injected           |
| Testing Support               | ✅ `pytest` per prompt        | ❌ manual                    |
| Multi-Backend Flexibility     | ✅ via `litellm_config.yaml`  | ❌ single provider hardcoded |
| Interactive Web UI            | ✅ `adk web .`                | ❌ none                      |

---

## 🧪 CI/CD Integration

You can integrate test coverage into GitHub Actions with the following:

```yaml
# .github/workflows/test.yml
name: Test Prompts
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

---

## 🧠 Use Cases

- Embedded system design co-piloting (e.g. Wi-Fi stack planning)
- Multi-stage software architecture design (requirements → modules)
- Educational systems teaching V-Model using LLMs
- Prompt engineering research on delegation and role-play

---

## 📊 Model Comparison (LiteLLM Backend)

| Provider   | Model            | Speed (tokens/sec) | Cost (est)      | Notes                       |
|------------|------------------|---------------------|------------------|-----------------------------|
| OpenAI     | `gpt-4`          | ⏳ slow (~15/s)     | 💸 High           | Very accurate, verbose      |
| OpenAI     | `gpt-3.5`        | ⚡ fast (~60/s)     | ✅ Low            | Less context window         |
| Ollama     | `llama3` local   | ⚡⚡ local (~80/s)   | 🆓 Free (CPU/GPU) | Can be run offline          |
| Anthropic  | `claude-3-opus`  | ⏳ medium (~20/s)   | 💸 High           | Good for summarization      |

---

## 📸 Screenshot Example (Web UI)

![ADK Web UI](https://raw.githubusercontent.com/google/adk-samples/main/images/web-ui.png)

> Note: Image is for illustration; replace with your live version if hosted.

---

## 🚧 Current Limitations

- ❌ No long-term memory persistence between sessions
- ❌ Limited to single user per session
- ❌ No guardrails or content moderation (out-of-the-box)
- ❌ ADK’s Web UI lacks markdown or rich output rendering

---

## 🌱 Future TODOs

- [ ] Add context-based agent activation (e.g. skip if state is complete)
- [ ] Add visualization of output (render HLD/module map into diagram)
- [ ] Integrate `tests/` with CI/CD pipeline (GitHub Actions)
- [ ] Add API layer for embedding in external workflows
- [ ] Memory persistence across sessions
- [ ] Auto-evaluation of generated code (unit tests)

---

## ✅ Summary

This ADK-powered multi-agent system enables fast, structured ideation and design for complex software workflows. It abstracts away state management, memory flow, prompt formatting, and multi-model orchestration.

While early-stage, it offers a promising architecture for future self-organizing LLM systems.

