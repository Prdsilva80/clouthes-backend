# clouthes-back/src/routes/returns_routes.py

from fastapi import APIRouter
from ..controllers.returns_controller import request_return, get_return

router = APIRouter()

router.post("/", response_model=dict)(request_return)
router.get("/{return_id}", response_model=dict)(get_return)
