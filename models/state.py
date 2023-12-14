#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    if storage_type != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns the list of City objects
            linked to the current State
            """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
