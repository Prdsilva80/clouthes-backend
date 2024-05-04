# clouthes-back/src/routes/user_routes.py

from fastapi import APIRouter
from ..controllers.user_controller import get_user, update_user_info

router = APIRouter()

router.get("/{user_id}", response_model=dict)(get_user)
router.put("/{user_id}", response_model=dict)(update_user_info)
