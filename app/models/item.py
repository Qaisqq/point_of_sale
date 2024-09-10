from sqlalchemy import Boolean, Column, Integer, String, BOOLEAN, ForeignKey, text, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base


class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    pcs = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=True)
    unit_cost = Column(Integer, nullable=True)
    discount = Column(BOOLEAN, nullable=True)
    discount_amount = Column(Integer, nullable=True)
    discount_precentege = Column(Integer, nullable=True)
    alias = Column(String, nullable=True)
    printer = Column(String, nullable=True)
    img_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by_id = Column(Integer, nullable=True)#ForeignKey("users.id", ondelete="CASCADE"), nullable=True) < implement this when creating user api
    provider = Column(String, nullable=True)
    comment = Column(String, nullable=True)
    is_available = Column(Boolean, nullable=True)
    has_variation = Column(Boolean, nullable=True)
    on_sale = Column(Boolean, nullable=True)
    category_id = Column(Integer, ForeignKey('categories.category_id', ondelete='SET NULL'))



#Dependecies for FKs and Relations
    # Define relationship to the Category model
    category = relationship("Category", back_populates="items")

    # Define the one-to-many relationship with OrderItems
    order_items = relationship("OrderItems", back_populates="items")