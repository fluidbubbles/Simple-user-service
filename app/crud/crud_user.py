from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserBase, UserUpdate, UserCreate
from app import crud


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get(self, db: Session, id: Optional[int] = None, fullname: Optional[str] = None) -> Optional[User]:
        if id:
            db_obj = super().get(db, int(id))
        else:
            db_obj = db.query(User).filter(User.fullname == fullname).first()
        return db_obj

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        fullname = f'{obj_in.first_name} {obj_in.last_name}'
        db_obj = db.query(User).filter(User.fullname == fullname).first()

        if db_obj:
            raise HTTPException(status_code=400, detail="Item already exists")

        user_in = UserBase(
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
        )
        new_user = super().create(db, obj_in=user_in)

        for email in obj_in.emails:
            crud.email.create(db, user_id=new_user.id, email=email)

        for num in obj_in.phone_nums:
            crud.phone.create(db, user_id=new_user.id, phone_no=num)

        return new_user


user = CRUDUser(User)
