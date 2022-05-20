from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationshipword
from app.db.base_class import Base


class Phone(Base):
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    user = relationship("User", back_populates="phone_numbers")
