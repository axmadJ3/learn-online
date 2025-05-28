import re
import uuid

from fastapi import HTTPException

from pydantic import BaseModel, EmailStr, field_validator


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        """tels pydantic to convert any non dict obj to json"""
        
        orm_mode = True
    


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
        
        
class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    
    @field_validator('name', mode="after")
    @classmethod
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value
        
    @field_validator('surname', mode="before")
    @classmethod
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Surname should contains only letters"
            )
        return value
    