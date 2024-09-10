from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ItemVariation(Base):
    __tablename__ = "item_variations"

    variation_id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    price = Column(Integer, nullable=False)
    variation = Column(String, nullable=True)


#Dependecies for FKs and Relations
    # Define relationship to the Item model
    items = relationship("Item", back_populates="item_variations")