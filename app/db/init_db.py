import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.data import EMAILS, PHONE_NUMS

logger = logging.getLogger(__name__)

FIRST_USER = 1


def init_db(db: Session) -> None:
    if FIRST_USER:
        user = crud.user.get(db, id=FIRST_USER)
        if not user:
            user_in = schemas.UserCreate(
                first_name="user1",
                last_name="first",
            )
            user = crud.user.create(db, obj_in=user_in)
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{FIRST_USER} already exists. "
            )
        if not user.emails:
            for email in EMAILS:
                crud.email.create(db, user_id=user.id, email=email["email"])

        if not user.phone_numbers:
            for phone_no in PHONE_NUMS:
                crud.phone.create(db, user_id=user.id, phone_no=phone_no["phone_no"])
