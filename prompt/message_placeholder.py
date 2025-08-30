## these messsages placeholder could be used when we had asking something earlier .. and we are asking some thing related to the previous thing agian .. then we could provide that informationo only with the prompt and this will help in generating the context with the query

# ya we could also use the memory but that require the whole memory to be passed to the prompt each time 

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history')
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)