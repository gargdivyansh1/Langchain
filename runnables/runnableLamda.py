# for creating a python funciton into runnable and then it would be ablle to make chain with others 

from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
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

parser = StrOutputParser()

joke_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
})

combined_chain = RunnableSequence(joke_generation_chain, parallel_chain)

print(combined_chain.invoke({'topic': 'women'}))

combined_chain.get_graph().print_ascii()