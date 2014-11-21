from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Projection(Base):
    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movies.id"))
    movie = relationship("Movie", backref="projections")
    type = Column(String)
    date = Column(String)
    time = Column(String)
