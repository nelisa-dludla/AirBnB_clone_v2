#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class Amenity(BaseModel):
    ''' class for Amenity '''
    name = Column(String(128), nullable=False)
