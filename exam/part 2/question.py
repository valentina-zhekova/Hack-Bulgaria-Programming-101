from connection import Base
from sqlalchemy import Column, String, Float, Integer


class Question(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True)
    question = Column(String, unique=True)
    answer = Column(Float)
