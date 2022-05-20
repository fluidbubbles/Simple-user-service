from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app import deps


router = APIRouter()


@router.get("", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user(user_id: Optional[int] = None, fullname: Optional[str] = None, db: Session = Depends(deps.get_db)):

    if not(user_id or fullname):
        raise HTTPException(status_code=403, detail="No query parameters")

    user = crud.user.get(db, id=user_id, fullname=fullname)
    emails = [mail.email for mail in user.emails]
    phone_nums = [num.number for num in user.phone_numbers]
    user = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "id": user.id,
        "emails": emails,
        "phone_nums": phone_nums
    }
    return user


@router.post("", status_code=status.HTTP_201_CREATED)
def add_user(user: schemas.UserCreate,
             db: Session = Depends(deps.get_db)):

    response = crud.user.create(db, obj_in=user)
    return response


@router.post("/append", status_code=status.HTTP_201_CREATED)
def append_contacts(user_id: int,
                    phone_no: Optional[str] = None,
                    email: Optional[str] = None,
                    db: Session = Depends(deps.get_db)):

    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if email:
        crud.email.create(db, user_id=user.id, email=email)

    if phone_no:
        crud.phone.create(db, user_id=user.id, phone_no=phone_no)

    return {"message": "successfully created", "status": 201}


@router.put("/edit_contact", status_code=status.HTTP_200_OK)
def edit_contact(user_id:  int,
                 phone_data: Optional[schemas.PhoneUpdate] = None,
                 email_data: Optional[schemas.EmailUpdate] = None,
                 db: Session = Depends(deps.get_db)):

    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_email, updated_phone = None, None
    if email_data:
        email = crud.email.get(db, id=email_data.id)
        if email:
            updated_email = crud.email.update(db, db_obj=email, obj_in=email_data)

    if phone_data:
        phone = crud.phone.get(db, id=phone_data.id)
        if phone:
            updated_phone = crud.phone.update(db, db_obj=phone, obj_in=phone_data)

    return updated_phone, updated_email


@router.delete("", status_code=status.HTTP_200_OK)
def delete_user(user_id: int,
                db: Session = Depends(deps.get_db)):

    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    crud.user.remove(db, id=user.id)
    return user
