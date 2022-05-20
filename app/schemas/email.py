from pydantic import BaseModel


class EmailBase(BaseModel):
    email: str


class EmailCreate(EmailBase):
    email: str
    user_id: int


class EmailUpdate(EmailBase):
    id: int
