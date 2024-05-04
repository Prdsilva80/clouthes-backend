# clouthes-back/src/routes/order_routes.py

from fastapi import APIRouter
from ..controllers.order_controller import place_order, get_order

router = APIRouter()

router.post("/", response_model=dict)(place_order)
router.get("/{order_id}", response_model=dict)(get_order)
