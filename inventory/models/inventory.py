#!/user/bin/env python3
"""location module"""
from models.basemodel import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Inventory(BaseModel):
    """location class setup with one to many relationship"""
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(Integer, ForeignKey("locations.id"))
    chemical = Column(String(60), ForeignKey("chemicals.batch_number"))
    no_of_sacks = Column(Float)
    no_of_gal = Column(Float)
    no_of_drums = Column(Float)
