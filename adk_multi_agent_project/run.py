import os
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from workflows.design_pipeline import agent as pipeline
from google.genai.types import Part, UserContent

load_dotenv()

runner = InMemoryRunner(agent=pipeline)
session = runner.session_service.create_session(app_name="multi-agent-demo", user_id="demo-user")

print("\n🧠 請輸入你的 Wi-Fi 功能需求 (例如: 支援 frame aggregation)：")
user_input = input("👉 ")

content = UserContent(parts=[Part(text=user_input)])
for event in runner.run(user_id=session.user_id, session_id=session.id, new_message=content):
    for part in event.content.parts:
        print("\n🤖 輸出:", part.text)
