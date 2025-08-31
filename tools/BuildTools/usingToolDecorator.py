from langchain_core.tools import tool

## this is here where we are simply declaring the function
# def multiply(a, b):
#     """Multipy two numbers"""
#     return a * b

## but it is adviced to make the tools with the type hints 
# def multiply(a: int, b: int) -> int:
#     """Multipy two numbers"""
#     return a * b

## now add the tool decorator
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b 

result = multiply.invoke({'a' : 2, 'b': 4})

print(result)