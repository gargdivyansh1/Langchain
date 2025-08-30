from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

result = model.invoke("What is the weather of city Gujrat?")

print(result)
print(result.content)