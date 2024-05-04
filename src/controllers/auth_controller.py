# clouthes-back/src/controllers/auth_controller.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from ..services.auth_service import authenticate_user, create_access_token

router = APIRouter(prefix="/auth")

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=UserOut)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(user.id)
    return {"access_token": token}
