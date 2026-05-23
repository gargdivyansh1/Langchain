from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview")

result = llm.invoke(input="What is the name of PM of INDIA?")

print(result)