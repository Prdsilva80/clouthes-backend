# clouthes-back/src/services/order_service.py

from ..database.db import SessionLocal
from ..models.order import Order, OrderItem

# Criar novo pedido
def create_order(order_data):
    db = SessionLocal()
    order = Order(user_id=order_data.user_id, status="Pending")
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in order_data.items:
        order_item = OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity)
        db.add(order_item)

    db.commit()
    return order.id

# Obter pedido por ID
def get_order_by_id(order_id: int):
    db = SessionLocal()
    return db.query(Order).filter(Order.id == order_id).first()
