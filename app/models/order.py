from sqlalchemy import Column, Integer, String, text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

#enum defintion for column
order_type_enum = Enum('takeout', 'delivery', 'table', name='order_type_enum', create_type=True)

class Order(Base):
    __tablename__ = "orders"

    order_uid = Column(UUID(as_uuid=True), unique=True,primary_key=True, default=uuid.uuid4, nullable=False)
    id = Column(Integer, nullable=False, index=True)
    status = Column(String, nullable=True, default='Open')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by_id = Column(Integer, nullable=True)#ForeignKey("users.id", ondelete="CASCADE"), nullable=True) < implement this when creating user api
    order_type = Column(order_type_enum, nullable=False)
    table_id = Column(Integer, nullable=True)#FK implement, when user implemntation
    discount = Column(Integer, nullable=True)
    discount_amount = Column(Integer, nullable=True)
    discount_precentege = Column(Integer, nullable=True)
    amount_before_discount = Column(Integer, nullable=True) #implement logic
    amount_after_discount = Column(Integer, nullable=True) #implement logic
    delievered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) #implement correct timestamp
    closed_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) #implement correct timestamp

#Dependecies for FKs and Relations
    order_items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    tables = relationship("DinerTable", back_populates="current_order")



