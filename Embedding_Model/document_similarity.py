from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "Hello!! What is your name?",
    "Hi!! My name is Divyansh Garg. What is your name?",
    "Myself LangChain. How are you?",
    "I am fine. What about you?",
    "I am also fine."
]

query = "Hello everyone, my name is Divyansh Garg."

load_dotenv()

# now make embedding model
model = "sentence-transformers/all-MiniLM-L6-v2"

llm = HuggingFaceEndpointEmbeddings(
    model=model,
    task="feature-extraction",   
)

# now make embeddings
doc_embeddings = llm.embed_documents(documents)
query_embedding = llm.embed_query(query)

similarity = cosine_similarity([query_embedding], doc_embeddings)[0] #type:ignore
# print(similarity)


# now we have to fetch the required document which has the maximum cosine similarity
# so for that we have to get he maximum of them 
min = -1
index = -1

i = 0
for score in similarity:
    if(score > min):
        min = score 
        index = i
    i = i+1
    
# print(min)
# print(index)

# now we got the index of the required document, so we will fetch it from the documents
print(f"The similarity score is: {min}")
print(query)
if(index == -1): print("No document is similar to query raised")
else: print(documents[index])

# i = 1
# for emb in embeddings:
#     print(i)
#     print(emb)
#     i = i+1
#     print("\n")
