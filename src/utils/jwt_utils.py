# clouthes-back/src/utils/jwt_utils.py

from jose import jwt, JWTError
from datetime import datetime, timedelta
import os
from typing import Optional

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Função para criar token JWT
def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar e decodificar token JWT
def decode_jwt_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if payload.get("exp") >= datetime.utcnow() else None
    except JWTError:
        return None
