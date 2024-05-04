# clouthes-back/src/services/user_service.py

from ..database.db import SessionLocal
from ..models.user import User

# Obter usuário por ID
def get_user_by_id(user_id: int):
    db = SessionLocal()
    return db.query(User).filter(User.id == user_id).first()

# Atualizar informações do usuário
def update_user(user_id: int, user_data):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if user_data.name:
            user.name = user_data.name
        if user_data.email:
            user.email = user_data.email
        db.commit()
        return True
    return False
