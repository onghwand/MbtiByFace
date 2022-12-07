from sqlalchemy import Column, Integer, String, Float, Boolean

from database import Base

class Celebrity(Base):
    __tablename__ = "celebrity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mbti = Column(String, nullable=False)
    image_url = Column(String, nullable=False)