from bunnet import Document as BunnetDocument
from beanie import Document as BeanieDocument
from pydantic import BaseModel, constr, validator
from typing import  Union
import hashlib

class UserModel(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class AddUser(UserModel):
    password: constr(min_length=8)

    @validator("password")
    def validate_password_complexity(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter.")
        return value

    @validator("password")
    def hash_password(cls, value):
        hashed_password = hashlib.sha256(value.encode()).hexdigest()
        return hashed_password

class DocumentUser(UserModel):
    class Settings:
        name = "user"


class UserBunnet(DocumentUser, BunnetDocument):
    pass


class UserBeanie(DocumentUser, BeanieDocument):
    pass
