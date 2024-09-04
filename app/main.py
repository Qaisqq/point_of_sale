from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.category import Category
from app.routers import item
from .models.order import Order
from app.models.item import Item
from .models.order_items import OrderItems
from .database import engine
from .routers import order, category
from .config import Settings

# Create tables
Category.__table__.create(bind=engine, checkfirst=True)
Order.__table__.create(bind=engine, checkfirst=True)
Item.__table__.create(bind=engine, checkfirst=True)
OrderItems.__table__.create(bind=engine, checkfirst=True)



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(order.router)
app.include_router(item.router)
app.include_router(category.router)


@app.get("/") 
def root():
    return {"message": "Welcome to my API"}

settings = Settings()