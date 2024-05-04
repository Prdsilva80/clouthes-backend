# clouthes-back/src/controllers/returns_controller.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.returns_service import initiate_return, get_return_by_id

router = APIRouter(prefix="/returns")

class ReturnIn(BaseModel):
    order_id: int
    reason: str

@router.post("/")
async def request_return(return_data: ReturnIn):
    return_id = initiate_return(return_data)
    if not return_id:
        raise HTTPException(status_code=400, detail="Unable to initiate return")
    return {"return_id": return_id}

@router.get("/{return_id}")
async def get_return(return_id: int):
    return_data = get_return_by_id(return_id)
    if not return_data:
        raise HTTPException(status_code=404, detail="Return not found")
    return return_data
