# clouthes-back/src/services/auth_service.py

from passlib.context import CryptContext
from jose import jwt
import os
from datetime import datetime, timedelta

# Configuração da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Função para verificar senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para hashear senha
def get_password_hash(password):
    return pwd_context.hash(password)

# Função para autenticar usuário
def authenticate_user(username: str, password: str):
    # Exemplo de busca de usuário fictício, substitua com acesso ao banco de dados
    user = {"username": "test_user", "password": "$2b$12$abcd1234"}
    if not user or not verify_password(password, user["password"]):
        return False
    return user

# Função para gerar token de acesso
def create_access_token(user_id: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user_id, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
