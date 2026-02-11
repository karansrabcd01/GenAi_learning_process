from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Configure with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# List all available models
print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")