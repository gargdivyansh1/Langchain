# this internally uses the request for fetching the url and beautifulsoup 

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(r'https://www.cdc.gov/hearher/index.html')

docs = loader.load()

print(docs[0].page_content.strip())