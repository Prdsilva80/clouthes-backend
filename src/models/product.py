# clouthes-back/src/models/product.py

from sqlalchemy import Column, Integer, String, Float, Boolean
from ..database.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    available = Column(Boolean, default=True)
