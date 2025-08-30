# the pypdfloader will return the document of each page of the pdf

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'DataLoader\PyPDFLoader\Emotion.pdf')

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)