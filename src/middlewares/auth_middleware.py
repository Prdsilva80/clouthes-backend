# clouthes-back/src/middlewares/auth_middleware.py

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import os

# Obter chave secreta e algoritmo a partir de variáveis de ambiente
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = 'HS256'

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid authentication scheme.')
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail='Invalid token or expired token.')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid authorization code.')

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = jwt.decode(jwtoken, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            is_token_valid = False
        else:
            is_token_valid = True
        return is_token_valid

# Função utilitária para verificar tokens
def verify_jwt_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except JWTError:
        return False
