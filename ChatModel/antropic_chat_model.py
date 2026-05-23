from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620") # type: ignore

# Invoke the model with a message
result = model.invoke("What is the capital of France?")

# Print the full result object and just the content
print("Full Result:")
print(result)
print("\nContent Only:")
print(result.content)
