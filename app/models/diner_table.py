from sqlalchemy import  Column, Integer, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base


# Define the ENUM type for table status
status_enum = Enum('occupied', 'vacant', 'reserved', name='status_enum', create_type=True)


class DinerTable(Base):
    __tablename__ = 'diner_tables'

    table_id = Column(Integer, primary_key=True, nullable=False)
    status = Column(Enum(status_enum), nullable=False)
    current_order_id = Column(Integer, ForeignKey('orders.uid'), nullable=True)

#Dependecies for FKs and Relations
    current_order = relationship("Order", back_populates="tables", foreign_keys=[current_order_id])


