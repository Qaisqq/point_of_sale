from sqlalchemy.ext.declarative import declarative_base
from .order import Order
from .item import Item
from .order_items import OrderItems

Base = declarative_base()