from langchain.schema.runnable import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "Write a joke about topic {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain this joke {joke}',
    input_variables=['joke']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model , parser)

print(chain.invoke({'topic': 'computer'}))

