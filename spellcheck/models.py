from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String, index=True)
    fixed_text = Column(String, index=True)
    train = Column(Boolean, default=False)
