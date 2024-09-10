import datetime
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class OrderBase(BaseModel):
    status: Optional[str] = None
    items: List[int]
    created_by: Optional[int] = None
    # status: Optional[bool] = None
    table_id: Optional[int] = None
    discount: Optional[bool] = None
    amount_before_discount: Optional[int] = None
    amount_after_discount: Optional[int] = None

    class Config:
        from_attributes = True


class OrderCreate(OrderBase):

    class Config:
        from_attributes = True

class OrderResponse(OrderBase):
    id: int
    items: List[int]

    class Config:
        from_attributes = True

class OrderUpdate(OrderBase):
    items: Optional[List[int]] = None
    items: List[int] = None
    takeout: Optional[bool] = None
    table_id: Optional[int] = None
    discount: Optional[bool] = None