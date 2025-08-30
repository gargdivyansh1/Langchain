from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class required(BaseModel):

    joke_about_the_scenario: str = Field(description="Write a joke which is depcting the situation")
    summary : str = Field(description="Give the summary of the situation")
    sentiment : Literal['positive', 'negative', 'neutral'] = Field(default='neutral', description='The sentiment of the sentence')
    joke : Optional[str] = Field(default=None, description='Give a non-veg joke for the situation is possible to generate by the sentence context.')
    time : Optional[int] = Field(default=None, description='Give the value of time is provided in the sentence')

structured_model = model.with_structured_output(required)

result = structured_model.invoke("This is a very bad movie, or can say the worst movie that I have ever seen in my entire life.")

print(result)
print(result.summary)