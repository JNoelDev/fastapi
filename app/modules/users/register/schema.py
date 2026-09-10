from pydantic import BaseModel,Field,EmailStr
from datetime import datetime
import uuid


class Register(BaseModel):
    first_name : str = Field(min_length=4,max_length=20)
    last_name:str = Field(min_length=4,max_length=20)
    email:EmailStr
    password:str


class ResponseRegister(BaseModel):
    model_config = {"from_attributes":True}
    userd_id: uuid.UUID
    first_name:str
    last_name:str
    date:datetime