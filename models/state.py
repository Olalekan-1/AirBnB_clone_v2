#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
# from models.city import City

db = os.getenv("HBNB_TYPE_STORAGE") == 'db'

if db:
    # from models.city import City

    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship(
                'City', cascade='all, delete-orphan',
                backref='state')
else:
    from models import storage

    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            from models import storage
            return [city for key, city in storage.all().items()
                    if key.startswith("City") and
                    city.state_id == self.id]
