# clouthes-back/src/routes/catalog_routes.py

from fastapi import APIRouter
from ..controllers.catalog_controller import list_products, get_product

router = APIRouter()

router.get("/products")(list_products)
router.get("/products/{product_id}")(get_product)
