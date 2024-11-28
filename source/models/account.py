import pdb
from bunnet import Document as BunnetDocument, Link as BunnetLink
from beanie import Document as BeanieDocument, Link as BeanieLink
from pydantic import BaseModel
from typing import Optional

# ------------ My customs modus ------------ #
from .user import UserBunnet, UserBeanie


class Data(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    status: Optional[str] = None
    type_user: Optional[str] = None
    user_access: Optional[str] = None
    block_time: Optional[int] = None
    change_password: Optional[bool] = None
    cluster: Optional[str] = None

    def model_dump(self):
        return self.dict()


class Information(BaseModel):
    name: Optional[str] = None
    bio: str = None
    phone_number: Optional[str] = None
    birthday: Optional[int] = None
    gender: Optional[str] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    is_professional: Optional[bool] = None
    profile_pic_url: Optional[str] = None
    email: Optional[str] = None

    def model_dump(self):
        return self.dict()

class AccountModel(BaseModel):
    hidden: Optional[bool] = False
    user_info: Optional[Information]
    user_data: Optional[Data]

    def model_dump(self):
        return self.dict()


class DocumentAccount(AccountModel):
    class Settings:
        name = "accounts"


class AccountBunnet(DocumentAccount, BunnetDocument):
    user: Optional[BunnetLink[UserBunnet]] = None


    def model_dump(self):
        return self.dict()


class AccountBeanie(DocumentAccount, BeanieDocument):
    user: Optional[BeanieLink[UserBeanie]] = None

    def model_dump(self):
        return self.dict()
