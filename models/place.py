#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table(
            "place_amenity", Base.metadata,
            Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
            Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
        )

class Place(BaseModel, Base):
    """ A place to stay """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete-orphan", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False,back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """Returns all reviews of a place"""
        all_rev = models.storage.all("Review").values()
        plRev = [
            review for review in all_rev
            if review.place_id == self.id
        ]
        return plRev
    
    @property
    def amenities(self):
        """Returns all amenities linked to a place"""
        return self.amenity_ids
    
    @amenities.setter
    def amenities(self, obj=None):
        """Appends obj to amenity_ids"""
        if (
            isinstance(obj, models.amenity.Amenity) and obj.id not in self.amenity_ids
        ):
            self.amenity_ids.append(obj.id)