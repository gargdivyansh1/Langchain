## this is used when we want to return the same tthing without any manipulation 
## like we want the output of the first and second step both .. 

from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
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

joke_gen_chain = RunnableSequence(prompt1, model, parser)

paralled_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'summary' : RunnableSequence(prompt2, model , parser)
})

final_chain = RunnableSequence(joke_gen_chain, paralled_chain)

print(final_chain.invoke({'topic' : 'women'}))

final_chain.get_graph().print_ascii()
