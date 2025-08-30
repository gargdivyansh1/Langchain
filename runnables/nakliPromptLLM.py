# as when making prompt we use to call the format method for filling the input values

from naklillm import NakliLLM

class NakliLLMPrompt:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
template = NakliLLMPrompt(
    template = "Write a {length} poem about {topic}",
    input_variables=['length', 'topic']
)

print(template.format({'length': 'short', 'topic': 'india'}))

prompt = template.format({'length': 'short', 'topic': 'india'})

## now here we created the prompt (nakli) .. and previously we had created the LLM (nakli) .. so now we can pass this prompt into the llm and then call the predict method of the llm .. this will give the desired output

llm = NakliLLM()

llm.predict(prompt)