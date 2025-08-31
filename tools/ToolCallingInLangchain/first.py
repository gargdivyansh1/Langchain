from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()

model = ChatOpenAI()

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

## Tool Binding

## now binding tools with the llm 
llm_with_tools = model.bind_tools([multiply])

# ##print(llm_with_tools.invoke("HI how are you?"))

# ## output -- content="Hello! I'm here and ready to help. How can I assist you today?" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 50, 'total_tokens': 68, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-CAad9ynYw1l2F82QVe7bJeweMztyR', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--8e4c6bf6-a66c-4547-80b1-3dc7ee405a6d-0' usage_metadata={'input_tokens': 50, 'output_tokens': 18, 'total_tokens': 68, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# ## Tool Calling

# # print(llm_with_tools.invoke("Multiply 3 with 5"))

# ## output -- content='' additional_kwargs={'tool_calls': [{'id': 'call_xDwBF3T6tLnhA2PFRmC6650X', 'function': {'arguments': '{"a": 3, "b": 5}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 32, 'prompt_tokens': 51, 'total_tokens': 83, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-CAadwgbGXwd8cbYH1FNdDfmIbfiZB', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None} id='run--35b0b2b1-4bf6-4ceb-a5e2-0c3ba301597e-0' tool_calls=[{'name': 'multiply', 'args': {'a': 3, 'b': 5}, 'id': 'call_xDwBF3T6tLnhA2PFRmC6650X', 'type': 'tool_call'}] usage_metadata={'input_tokens': 51, 'output_tokens': 32, 'total_tokens': 83, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}


# # print(llm_with_tools.invoke("Multiply 3 with 5").tool_calls[0])

# ## output -- {'name': 'multiply', 'args': {'a': 3, 'b': 5}, 'id': 'call_RPYLIIaf7Nt2jucLuO65LxFw', 'type': 'tool_call'}

# ## by this we got to know that LLM do not call the tool it give us advice that we could use this tool for the problem 

# results = llm_with_tools.invoke('multiply 3 with 5')
# # content='' additional_kwargs={'tool_calls': [{'id': 'call_uKKptqdtHLXUHSclbrpvP6Ov', 'function': {'arguments': '{"a":3,"b":5}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 51, 'total_tokens': 68, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-CAaisSqTk1tABwTfbkBQ0qvQZVl4B', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None} id='run--ec057234-4113-4b64-9cf6-1ecf65df7d84-0' tool_calls=[{'name': 'multiply', 'args': {'a': 3, 'b': 5}, 'id': 'call_uKKptqdtHLXUHSclbrpvP6Ov', 'type': 'tool_call'}] usage_metadata={'input_tokens': 51, 'output_tokens': 17, 'total_tokens': 68, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# required = results.tool_calls[0]
# # {'name': 'multiply', 'args': {'a': 3, 'b': 5}, 'id': 'call_0Vt4Vja2iQ8SQgAdxwTL2CdY', 'type': 'tool_call'}

# required_args = required['args']
# # {'a': 3, 'b': 5}

# ## now do the operation 
# print(multiply.invoke(required_args))
# # 15

# print(multiply.invoke(required))
# # ToolMessage(content='15' name='multiply' tool_call_id='call_7ji9ecwu6MHjq4Vsn0sbZckh' )

# ## now when we are sending the required .. then we are getting toolmessage in return .. now we could pass it to the llm and llm would understand the result

# ## now executing the whole thing together

query = HumanMessage("Multiply 2 and 3")

messages = [query]

result = llm_with_tools.invoke(messages)

messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

final_result = llm_with_tools.invoke(messages)

print(final_result)