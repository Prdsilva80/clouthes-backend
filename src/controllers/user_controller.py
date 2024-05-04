# clouthes-back/src/controllers/user_controller.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.user_service import get_user_by_id, update_user

router = APIRouter(prefix="/users")

class UserUpdate(BaseModel):
    name: str = None
    email: str = None

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
async def update_user_info(user_id: int, user_data: UserUpdate):
    updated = update_user(user_id, user_data)
    if not updated:
        raise HTTPException(status_code=400, detail="Unable to update user")
    return {"status": "success"}
