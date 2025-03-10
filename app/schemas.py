from datetime import datetime
from re import S
from pydantic import BaseModel, EmailStr, conint
from typing import Optional, Union


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Response(PostBase):
    id: int
    create_at: datetime
    owner_id: int
    owner: UserOut


class PostOut(BaseModel):
    Post: Response
    votes: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[Union[str, int]] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore

