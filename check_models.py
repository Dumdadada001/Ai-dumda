import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("사용 가능한 모델 목록을 확인합니다...")
try:
    models = client.models.list()
    for m in models:
        print(f"- {m.name} (지원: {m.supported_actions})")
except Exception as e:
    print(f"오류 발생: {e}")
