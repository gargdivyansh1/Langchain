from abc import ABC, abstractmethod
import random 

class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

class NakliLLM(Runnable):

    def __init__(self):
        print('LLM created')

    
    ## here we are invoking the abstract method which we have made in the Runnable class
    def invoke(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}


    def predict(self, prompt):

        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}
    

class NakliPrompt(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)
    
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
class NakliStrOutputParser(Runnable):

    def __init__(self):
        pass

    def invoke(self, input_dict):
        return input_dict['response']
    
class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data
    
template = NakliPrompt(
    template='Write a {length} poem about topic {topic}',
    input_variables=['length', 'topic']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain = RunnableConnector([template, llm, parser])

print(chain.invoke({'length': 'short', 'topic': 'india'}))



## making 2 differnt runnable and merging them 

template1 = NakliPrompt(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPrompt(
    template='Write the summary for this {response}',
    input_variables=['response']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm]) # this will return response 

chain2 = RunnableConnector([template2, llm , parser]) # this will give the final result 

final_chain = RunnableConnector([chain1, chain2])

print(final_chain.invoke({'topic': 'cricket'}))