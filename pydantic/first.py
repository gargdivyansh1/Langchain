from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    name : str 
    gender : str = 'male' # for providing the defalut values 
    age : Optional[int] = None 
    email : EmailStr
    cgpa : float = Field(gt = 0, lt = 5)

new_student = {'name': 'Divyansh', 'age': '20'}

student = Student(**new_student)

print(student)

## this could be said as the more stricted version of the typedict 
## here the value must be of the datatype provided 
## there is also one more thing called as type corsing -- it means if the int values is need to be passed and the user has some how passed it in the format of string like '89' .. so it will itself convert it into int 89 .. and for many other cases .. pydantic does this by its own 