from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.category import Category
from app.schemas.category import  CategoryResponse, CategoryCreate, CategoryUpdate

router = APIRouter(
    prefix = "/category",
    tags = ["category"]
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/{name}", response_model=CategoryResponse)
def get_category(name: str, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.name == name).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"category with name: {name} was not found")
    return category

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    category = db.query(Category).all()
    if category == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"there is no current categories")
    return category

@router.put("/{id}", response_model=CategoryResponse)
def update_category(id: int, updated_category: CategoryUpdate, db: Session = Depends(get_db)):
    category_query = db.query(Category).filter(Category.category_id == id)
    category = category_query.first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"category with id: {id} doesnt not exist")
    # if category.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized") 
    #later implementation
    update_data = updated_category.model_dump(exclude_unset=True)   # Only include fields that are not None

    for key, value in update_data.items():
        setattr(category, key, value)

    db.commit()
    return category

@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category_query = db.query(Category).filter(Category.category_id == id)
    category = category_query.first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"category with id: {id} doesnt not exist")
    # if category.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized") 
    #later implementation
    category_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)