from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class OrderItems(Base):
    __tablename__ = "order_items"
    
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    item_quantity = Column(Integer, default=1)
    comment = Column(String, nullable=True)
    variation = Column(String, nullable=True)
    price = Column(Integer, nullable = True)

    
    # Define the relationship with Orders and Items
    order = relationship("Order", back_populates="order_items")
    items = relationship("Item", back_populates="order_items")