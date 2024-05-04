# clouthes-back/src/services/catalog_service.py

from ..database.db import SessionLocal
from ..models.product import Product

# Obter todos os produtos
def get_all_products(category: str = None):
    db = SessionLocal()
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    return query.all()

# Obter produto por ID
def get_product_by_id(product_id: int):
    db = SessionLocal()
    return db.query(Product).filter(Product.id == product_id).first()
