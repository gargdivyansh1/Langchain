## this typedict is only for the representation purpose .. means there is no gurantee that if you demand for the string .. then you will be getting the string in the response 
## the llm can do the errors 

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import TypedDict, Literal, Annotated, Optional
import os

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# template = """
# You are a sentiment analyser, your work is to analyse the sentiment of the sentence provided.
# Majorly the sentence is from movie data.
# # Also generate a joke which kind of related to the sentence.

# <|user|> Sentence: {sentence}
# <|end|>
# <|assistant|>
# """

# input_prompt = PromptTemplate(
#     template=template,
#     input_variables=['sentence']
# )

## now before invoking the sentence we will be using the type dict for the required data type
class required(TypedDict):
    joke_about_the_scenario: str
    summary : str
    sentiment : Literal['positive', 'negative', 'neutral']
    joke : Annotated[str, "give the joke which kind of explaining the situation in funny way"]
    time : Annotated[Optional[int] , 'give the value of what time the sentence was said']

structured_model = model.with_structured_output(required)

# chain = input_prompt | structured_model

# result = chain.invoke({"sentence": "This is a very bad movie, or can say the worst movie that I have ever seen in my entire life."})

result = structured_model.invoke("This is a very bad movie, or can say the worst movie that I have ever seen in my entire life.")

print(result)
print(result['sentiment'])
print(result['summary'])
print(result['joke'])

## the main advantage of using the typedict is that we do not need to define the prompt explictily like what to do and what to return .. 
## this typedict handle this automatically and do the evaluation according to it .. and give us the desired results 

# but there is also one more thing .. as when i write the joke field also with the sentiment then it is not able to give the value of the joke and just writing the sentence in it directly 

## but this problem could be solved using the prompt ]
# what i found later is .. if the key is defined with more meanning then it also resolve the problem


## this could also be resolved using the annotations , ,like passing the thing wchih we want with the datatype

## we could also provide the keyword optional .. which means if the sentence does not have that value then no need to give it in result 