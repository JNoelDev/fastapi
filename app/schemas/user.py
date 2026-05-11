from pydantic import (
    BaseModel,EmailStr,SecretStr,ConfigDict,Field
    )
from datetime import datetime
from fastapi import Form
from .enums import Sex


"""inscription en locale"""
class UserCreateLocal(BaseModel):
    username : str
    email : EmailStr
    password : SecretStr = Field(min_length=8)
    pa : str 
    phone : str|None = None
    
    @classmethod
    def as_form(cls,
        username : str = Form(...),
        email : EmailStr = Form(...),
        password : SecretStr = Form(...),
        phone : str|None = Form(...),
        sexe : Sex = Form(default=None)
    ):
        
        return cls(
            username=username,
            email=email,password=password,
            phone=phone,sexe=sexe
            )

"""information après la verification"""   
class UserOut(BaseModel):
    id : int
    username : str
    code_user : str
    verified : bool
    created_at : datetime

    model_config=ConfigDict(from_attributes=True)

"""Utilisateur vu par recherche"""
class UserProfile_Public(BaseModel):
    full_name : str
    profile_picture : str
    code_user : str
    relationship_status : str

    model_config=ConfigDict(from_attributes=True) 



