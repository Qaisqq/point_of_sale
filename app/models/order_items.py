from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID

class OrderItems(Base):
    __tablename__ = "order_items"
    
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.order_uid'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    item_quantity = Column(Integer, default=1)
    comment = Column(String, nullable=True) #change to item_comment
    variation = Column(String, nullable=True)
    price = Column(Integer, nullable = True)

#Dependecies for FKs and Relations

    # Define the relationship with Orders and Items
    order = relationship("Order", back_populates="order_items")
    items = relationship("Item", back_populates="order_items")