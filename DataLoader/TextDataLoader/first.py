## Document{
    # page_content: "jghb",
    # metadata: "saew"
##}

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "Write the summary for the follwing text {text}",
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader(r'DataLoader\TextDataLoader\cricket.txt', encoding='utf-8')

docs = loader.load()

# print(len(docs))
# print(type(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'text': docs[0].page_content}))