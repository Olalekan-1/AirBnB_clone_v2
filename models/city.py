#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.state import State
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    import sqlalchemy
    from sqlalchemy import Column, String, ForeignKey
    from models.base_model import Base
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):

        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State", back_populates="cities")

else:
    class City(BaseModel):
        # The city class, contains state ID and name
        state_id = ""
        name = ""

if getenv("HBNB_TYPE_STORAGE") == "db":
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")

"""
class City(BaseModel, Base):
    This is the class for City
    Attributes:
        state_id: The state id
        name: input name
        #
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'))
    if getenv("HBNB_TYPE_STORAGE") == "db":
        state = relationship("State", back_populates="cities")


if getenv("HBNB_TYPE_STORAGE") == "db":
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")
"""
