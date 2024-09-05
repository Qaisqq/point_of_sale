from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True)
    name = Column(String, nullable=False, unique=True)  # Ensure this column is unique
    created_by = Column(Integer, nullable=True)  # Add ForeignKey for users when users table is implemented
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    img_url = Column(String, nullable=True)
    category_type = Column(String, nullable=True)
    parent_id = Column(Integer, nullable=True, default=None)
    parent_name = Column(String, nullable=True, default=None)


    # Define relationship to the Item model
    items = relationship("Item", back_populates="category")