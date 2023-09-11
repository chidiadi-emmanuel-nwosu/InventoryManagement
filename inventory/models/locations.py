#!/user/bin/env python3
"""location module"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship



location_additive = Table(
        "location_chemical",
        Base.metadata,
        Column(
            "location_id",
            Integer,
            ForeignKey('locations.id'),
            primary_key=True
            ),
        Column(
            "chemical_batch_number",
            String(30),
            ForeignKey('chemicals.batch_number'),
            primary_key=True
            )
        )

class Location(BaseModel):
    """location class setup with one to many relationship"""
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True, server_default='0')
    name = Column(String(30), nullable=False)
    inventory = relationship('Inventory', backref='location_name')
    additives = relationship('Chemical', secondary=location_additive, viewonly=False)
