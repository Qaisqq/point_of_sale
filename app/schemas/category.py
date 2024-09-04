from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    created_by: Optional[int] = None
    img_url: Optional[str] = None

    class Config:
        from_attributes = True

class CategoryCreate(CategoryBase):
    pass

    class Config:
        from_attributes = True

class CategoryResponse(CategoryBase):
    pass

    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    img_url: Optional[str] = None

    class Config:
        from_attributes = True

