from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Use the full model name with version
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.9)

result = model.invoke("What is the capital of India?")
print(result.content)