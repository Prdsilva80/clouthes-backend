# clouthes-back/src/controllers/catalog_controller.py

from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..services.catalog_service import get_all_products, get_product_by_id

router = APIRouter(prefix="/catalog")

@router.get("/products")
async def list_products(category: str = Query(None)):
    return get_all_products(category)

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
