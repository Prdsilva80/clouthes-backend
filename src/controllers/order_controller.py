# clouthes-back/src/controllers/order_controller.py

from fastapi import APIRouter, HTTPException, Depends
from ..services.order_service import create_order, get_order_by_id
from pydantic import BaseModel

router = APIRouter(prefix="/orders")

class OrderIn(BaseModel):
    product_id: int
    quantity: int
    user_id: int

@router.post("/")
async def place_order(order: OrderIn):
    order_id = create_order(order)
    if not order_id:
        raise HTTPException(status_code=400, detail="Unable to create order")
    return {"order_id": order_id}

@router.get("/{order_id}")
async def get_order(order_id: int):
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
