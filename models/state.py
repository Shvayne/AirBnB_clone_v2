#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City

type_storage = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if type_storage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        name = ""

    if type_storage != 'db':
        @property
        def cities(self):
            """returns city instances whose state id equal the current state_id"""
            aCities = models.storage.all(City)
            sCities = [
                city for city in aCities.values()
                if city.state_id == self.id
            ]
            return sCities
