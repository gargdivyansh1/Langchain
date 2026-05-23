from langchain_huggingface import HuggingFaceEmbeddings,HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = "sentence-transformers/all-MiniLM-L6-v2"

llm = HuggingFaceEndpointEmbeddings(
    model=model,
    task="feature-extraction",   
)

# result = llm.embed_query("Hello!! What is your name?")

documents = [
    "Hello!! What is your name?",
    "Hi!! My name is Divyansh Garg. What is your name?",
    "Myself LangChain. How are you?",
    "I am fine. What about you?",
    "I am also fine."
]

result = llm.embed_documents(documents)

print(str(result))