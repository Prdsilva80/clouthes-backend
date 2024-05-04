# clouthes-back/src/models/auth.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..database.db import Base

class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String, nullable=False, unique=True)
    expires_at = Column(DateTime)
