from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    receipts = relationship("Receipt", back_populates="user")

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    groceries = relationship("GroceryItem", back_populates="receipt")
    user = relationship("User", back_populates="receipts")

class GroceryItem(Base):
    __tablename__ = "groceries"
    id = Column(Integer, primary_key=True)
    receipt_id = Column(Integer, ForeignKey("receipts.id"))
    name = Column(String)
    price = Column(Float)
    quantity = Column(String, nullable=True)
    expiration_id = Column(Integer, ForeignKey("expirations.id"))
    receipt = relationship("Receipt", back_populates="groceries")

class Expiration(Base):
    __tablename__ = "expirations"
    id = Column(Integer, primary_key=True)
    item_name = Column(String, unique=True)
    estimated_days = Column(Integer)
