from connection import Base
from sqlalchemy import Column, Integer, String


class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    scores = Column(Integer)
