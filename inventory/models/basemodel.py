#!/user/bin/env python3
"""Base Model module"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """base class for chemica additives"""
    __abstract__ = True

    def save(self):
        """saves a new object to the table"""
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """deletes an object"""
        from models import storage
        storage.delete(self)
