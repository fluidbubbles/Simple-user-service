from pydantic import BaseModel


class PhoneBase(BaseModel):
    number: str


class PhoneCreate(PhoneBase):
    number: str
    user_id: int


class PhoneUpdate(PhoneBase):
    id: int
