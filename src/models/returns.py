# clouthes-back/src/models/returns.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..database.db import Base

class Return(Base):
    __tablename__ = 'returns'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, default='Pending')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
