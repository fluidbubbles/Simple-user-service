from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.db.base_class import Base


class User(Base):  # 1
    id = Column(Integer, primary_key=True, index=True)  # 2
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=True)
    emails = relationship("Email", cascade="all,delete-orphan", back_populates="user", uselist=True)
    phone_numbers = relationship("Phone", cascade="all,delete-orphan", back_populates="user", uselist=True)

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name

    class Config:
        orm_mode = True
