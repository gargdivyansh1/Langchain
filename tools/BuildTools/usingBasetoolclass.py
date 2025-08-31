from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = 'Multiply'
    description : str = "Mutiply two numbers"

    args_schema : Type[BaseModel] = MultiplyInput

    ## the name of the function here should be this only
    def _run(self, a: int, b: int) -> int:
        return a * b
    
multiply_tool = MultiplyTool()

result = multiply_tool({'a': 4, 'b': 8})

print(result)