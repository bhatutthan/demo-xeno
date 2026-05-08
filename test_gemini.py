import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

for model in ['gemini-2.0-flash-lite', 'gemini-flash-latest', 'gemini-2.5-flash', 'gemini-2.0-flash-001']:
    try:
        response = client.models.generate_content(
            model=model,
            contents='test'
        )
        print(f"{model}: SUCCESS")
        break
    except Exception as e:
        print(f"{model}: FAILED - {e}")
