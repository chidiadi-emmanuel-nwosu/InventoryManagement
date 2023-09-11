#!/user/bin/env python3
"""Chemical Additive module"""
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel


class Chemical(BaseModel):
    """base class for chemica additives"""
    __tablename__ = "chemicals"
    id = Column(Integer, autoincrement=True, server_default='1')
    item_code = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    product_code = Column(String(30), nullable=False)
    package_size = Column(String(30), nullable=False)
    manufacturer = Column(String(128))
    expiry_date = Column(Date)
    batch_number = Column(String(30), primary_key=True)
    inventory = relationship('Inventory', backref='additive')
    location = relationship('Location', secondary='location_additive')
