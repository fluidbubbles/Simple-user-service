from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Email(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    user = relationship("User", back_populates="emails")
