from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phone import Phone
from app.schemas.phoneNumber import PhoneBase, PhoneUpdate, PhoneCreate


class CRUDPhone(CRUDBase[Phone, PhoneBase, PhoneUpdate]):
    def create(self, db: Session, user_id: int, phone_no: str) -> Phone:
        phone_no_in = PhoneCreate(
            number=phone_no,
            user_id=user_id
        )
        super().create(db, obj_in=phone_no_in)


phone = CRUDPhone(Phone)
