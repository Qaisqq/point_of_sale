# from ast import Or
# from fastapi import APIRouter, Depends, HTTPException, status, Response
# from sqlalchemy.orm import Session
# from sqlalchemy.exc import SQLAlchemyError
# from typing import List
# from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
# from ..database import get_db
# from app.models import Order, OrderItems


# router = APIRouter(
#     prefix = "/order",
#     tags = ["order"]
# )


# @router.post("/")
# def create_order(order: OrderCreate, db: Session = Depends(get_db)):
#     # Create the Order
#     db_order = Order()
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)

#     finished_items = []
#     items = order.items

#     # Iterate over the items list
#     for item_id in items:
#         # Create a new OrderItems entry
#         existing_item = db.query(OrderItems).filter_by(order_id=db_order.id, item_id=item_id).first()
#         if existing_item:
#             # Increment the quantity if it already exists
#             existing_item.item_quantity += 1
#             db.commit()
#         else:
#             order_item = OrderItems(order_id=db_order.id, item_id=item_id)
#             db.add(order_item)
#             db.commit()
#             db.refresh(db_order)
#             print(f"Processing item with ID: {item_id}")
#             finished_items.append(item_id)

#     # Return response matching the schema
#     return f"ordered item ids: {finished_items}"


# @router.get("/")
# def get_orders(db: Session = Depends(get_db)):
#     orders = db.query(Order).all()
#     return orders



# @router.get("/{id}")
# def get_order(id: str, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == id).first()
#     order_items = db.query(OrderItems).filter(OrderItems.order_id == id).all()
#     if order == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"order with id: {id} was not found")
#     return order , order_items


# @router.put("/{id}", response_model=OrderUpdate)
# def update_order(id: int, updated_order: OrderUpdate, db: Session = Depends(get_db)):
#     order_query = db.query(Order).filter(Order.id == id)
#     order = order_query.first()
#     if order == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"order with id: {id} doesnt not exist")
#     # if category.owner_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized") 
#     #later implementation
#     update_data = updated_order.model_dump(exclude_unset=True)

#     for key, value in update_data.orders(): 
#         setattr(order, key, value)

#     db.commit()
#     return order_query.first()


# @router.delete("/{id}") 
# def delete_order(id: int, db: Session = Depends(get_db)):

#     # Delete OrderItems
#     db.query(OrderItems).filter(OrderItems.order_id == id).delete(synchronize_session=False)
#     db.commit()
#     # delete Order
#     db.query(Order).filter(Order.id == id).delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)