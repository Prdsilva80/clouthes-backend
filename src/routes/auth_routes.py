# clouthes-back/src/routes/auth_routes.py

from fastapi import APIRouter
from ..controllers.auth_controller import login

router = APIRouter()

router.post("/login", response_model=dict)(login)
