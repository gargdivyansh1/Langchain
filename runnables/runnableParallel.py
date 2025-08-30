from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= 'Generate a linkedin post caption for topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a tweet about the topci {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'linkedinPost': RunnableSequence(prompt1, model, parser),
    'tweet': RunnableSequence(prompt2, model, parser)}
)

prompt3 = PromptTemplate(
    template = 'give the rating of the generated linkedinpost {linkedinPost} and the tweet {tweet} ',
    input_variables=['linkedinPost', 'tweet']
)

sequential_chain = RunnableSequence(prompt3, model, parser)

combined_chain = RunnableSequence(parallel_chain, sequential_chain)

print(combined_chain.invoke({'topic': 'India losses againt Pakistan'}))

combined_chain.get_graph().print_ascii()