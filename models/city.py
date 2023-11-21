#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    import sqlalchemy
    from sqlalchemy import Column, String, ForeignKey
    from models.base_model import Base
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):

        __tablename__ = 'cities'

        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
