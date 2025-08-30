from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = OpenAIEmbeddings()

## here we are creating the vector embeddings

vectorstore = Chroma(
    embedding_function = OpenAIEmbeddings(),
    persist_directory = 'my_chrome_db',
    collection_name="my_collection"
)

vectorstore.add_documents(documents)

retriever = vectorstore.as_retriever(search_kwargs = {'k': 2})

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)