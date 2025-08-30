from naklillm import NakliLLM
from nakliPromptLLM import NakliLLMPrompt

class NakliChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        resutl = self.llm.predict(final_prompt)

        return resutl['response']
    
llm = NakliLLM()

template = NakliLLMPrompt(
    template = "Write a {length} poem about {topic}",
    input_variables=['length', 'topic']
)
    
chain = NakliChain(llm , template)

chain.run({'length': 'short', 'topic': 'india'})