import random 

# as we call the predict method to get the output 

class NakliLLM:

    def __init__(self):
        print("LLM created")

    def predict(self, input):
        response_list = [
            'Delhi is the capital of Inida',
            "IPL is a cricket league",
            "He is a very good boy."
        ]

        return {'response': random.choice(response_list)}
    
value = NakliLLM()

print(value.predict('What is the capital of India?'))