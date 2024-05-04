# clouthes-back/src/services/returns_service.py

from ..database.db import SessionLocal
from src.models.returns import Return

# Iniciar processo de devolução
def initiate_return(return_data):
    db = SessionLocal()
    ret = Return(order_id=return_data.order_id, reason=return_data.reason, status="Pending")
    db.add(ret)
    db.commit()
    db.refresh(ret)
    return ret.id

# Obter devolução por ID
def get_return_by_id(return_id: int):
    db = SessionLocal()
    return db.query(Return).filter(Return.id == return_id).first()
