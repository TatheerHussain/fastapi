from typing import Optional, List
from uuid import UUID, uuid4 
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str,Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID]= uuid4()
    first_name: str
    last_name: str
    email: str
    password: str
    mobile: str
    gender:Gender
    roles:List[Role]
    
    class Config:
        orm_mode = True