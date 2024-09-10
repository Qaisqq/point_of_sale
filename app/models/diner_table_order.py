from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class OrderItems(Base):
    __tablename__ = "order_items"
    
    table_id = Column(Integer, ForeignKey('diner_tables.table_id'), primary_key=True)
    table_status = Column(String, ForeignKey('diner_tables.status'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    order_status = Column(String, ForeignKey('orders.status'), primary_key=True)

#Dependecies for FKs and Relations

    # Define the relationship with Orders and Items
    diner_tables = relationship("DinerTable", back_populates="diner_table_order")
    order = relationship("Order", back_populates="diner_table_order")