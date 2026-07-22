from sqlalchemy import Column, Integer, Float, String
from app.db.base import Base

class MemberModel(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    length_m = Column(Float, nullable=False)
