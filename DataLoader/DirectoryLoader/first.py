from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = "books",
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load() -- it take lot more time hence we will be usin the lazy load
docs = loader.lazy_load()

# here we are using the pypdfloader ..hence each page will be extracted as document
print(docs)

for doc in docs:
    print(doc.page_content)
    pass