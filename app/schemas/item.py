from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    pcs: int
    price: int
    category_id: int
    weight: Optional[int] = None
    unit_cost: Optional[int] = None
    sale: Optional[bool] = None
    alias: Optional[str] = None
    printer: Optional[str] = None
    img_url: Optional[str] = None

    class Config:
        from_attributes = True

class ItemCreate(ItemBase):
    name: str
    pcs: int
    price: int

    class Config:
        from_attributes = True

class ItemResponse(ItemBase):
    name: str
    pcs: int
    price: int

    class Config:
        from_attributes = True

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    pcs: Optional[int] = None
    price: Optional[int] = None
    category_id: Optional[int] = None
    img_url: Optional[str] = None

    class Config:
        from_attributes = True