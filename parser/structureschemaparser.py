from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name='fact_1', description='fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description='fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description='fact e about the topic'),
    ResponseSchema(name = 'fact_4', description='fact 4 about the topic'),
]

# this we use when we want to define the response schema
# there is no validation of the schema .. it could be happen that the name field which has datatype string could have a value '34' as it is also a string
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give 4 facts about the topic {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic': 'black hole'})

print(result)