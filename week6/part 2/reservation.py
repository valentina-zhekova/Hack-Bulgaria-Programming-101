from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship


class Reservation(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("Projections.id"))
    projection = relationship("Projection", backref="reservations")
    row = Column(Integer, CheckConstraint("row >= 1" and "row <= 10"))
    col = Column(Integer, CheckConstraint("col >= 1" and "col <= 10"))
