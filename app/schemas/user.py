from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    emails: List[str] = []
    phone_nums: List[str] = []


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    emails: List[str] = []
    phone_nums: List[str] = []

    class Config:
        orm_mode = True
