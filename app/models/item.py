from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    pcs = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=True)
    unit_cost = Column(Integer, nullable=True)
    sale = Column(BOOLEAN, nullable=True)
    alias = Column(String, nullable=True)
    printer = Column(String, nullable=True)
    img_url = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey('categories.category_id', ondelete='SET NULL'))
    # Define relationship to the Category model
    category = relationship("Category", back_populates="items")

    # Define the one-to-many relationship with OrderItems
    order_items = relationship("OrderItems", back_populates="items")