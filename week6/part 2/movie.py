from connection import Base
from sqlalchemy import Column, Integer, String, Float


class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

    def __str__(self):
        return "[{}] - {} ({})".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()
