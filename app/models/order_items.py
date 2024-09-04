from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OrderItems(Base):
    __tablename__ = "order_items"
    
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    item_quantity = Column(Integer, default=1)
    
    # Define the relationship with Orders and Items
    order = relationship("Order", back_populates="order_items")
    items = relationship("Item", back_populates="order_items")