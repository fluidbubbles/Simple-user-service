from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.email import Email
from app.schemas.email import EmailUpdate, EmailCreate


class CRUDEmail(CRUDBase[Email, EmailCreate, EmailUpdate]):
    def create(self, db: Session, user_id: int, email: str) -> Email:
        email_in = EmailCreate(
            email=email,
            user_id=user_id
        )
        super().create(db, obj_in=email_in)


email = CRUDEmail(Email)
