from langchain_community.document_loaders import CSVLoader

# this will provide 1 document for 1 row
loader = CSVLoader(r'DataLoader\CSVLoader\Social_Network_Ads.csv')

docs = loader.load()

print(docs[0])