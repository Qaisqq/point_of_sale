from sqlalchemy import Boolean, Column, Integer, String, table, text
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True)
    status = Column(String, nullable=True, default='Open')
    delievered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #order.delivered_at = datetime.utcnow() < implement this on path operation of finishing order
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by = Column(Integer, nullable=True)#, ForeignKey("users.id", ondelete="CASCADE"), nullable=True) < implement this when creating user api
    takeout = Column(Boolean, nullable=True)
    table_id = Column(Integer, nullable=True)
    discount = Column(Boolean, nullable=True)
    amount_before_discount = Column(Integer, nullable=True)
    amount_after_discount = Column(Integer, nullable=True)

    order_items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")