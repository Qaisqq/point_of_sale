# from sqlalchemy.orm import Session
# from fastapi import APIRouter, Depends, HTTPException, status, Response
# from sqlalchemy.orm import Session
# from ..database import get_db
# from ..database import get_db
# from app.models import Item
# from ..schemas.item import ItemBase, ItemCreate, ItemResponse, ItemUpdate


# router = APIRouter(
#     prefix = "/item",
#     tags = ["item"]
# )


# @router.post("/",status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
# def create_item(item: ItemCreate, db: Session = Depends(get_db)):
#     new_item = Item(**item.model_dump())
#     db.add(new_item)
#     db.commit()
#     db.refresh(new_item)
#     return new_item

# @router.get("/{name}", response_model=ItemResponse)
# def get_item(name: str, db: Session = Depends(get_db)):
#     item = db.query(Item).filter(Item.name == name).first()
#     if item == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"item with name: {name} was not found")
#     return item

# @router.get("/")
# def get_item(db: Session = Depends(get_db)):
#     item = db.query(Item).all()
#     if item == []:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"there is no current item")
#     return item

# @router.put("/{id}", response_model=ItemResponse)
# def update_item(id: int, updated_item: ItemUpdate, db: Session = Depends(get_db)):
#     item_query = db.query(Item).filter(Item.id == id)
#     item = item_query.first()
#     if item == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"item with id: {id} doesnt not exist")
#     # if category.owner_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized") 
#     #later implementation
#     update_data = updated_item.model_dump(exclude_unset=True)

#     for key, value in update_data.items():
#         setattr(item, key, value)

#     db.commit()
#     return item_query.first()

# @router.delete("/{id}")
# def delete_item(id: int, db: Session = Depends(get_db)):
#     item_query = db.query(Item).filter(Item.id == id)
#     item = item_query.first()
#     if item == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Item with id: {id} doesnt not exist")
#     # if category.owner_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized") 
#     #later implementation
#     item_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)