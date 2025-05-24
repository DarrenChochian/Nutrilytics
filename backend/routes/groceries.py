from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import GroceryItem
from fastapi.responses import JSONResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get-groceries")
def get_groceries(user_id: int, db: Session = Depends(get_db)):
    groceries = db.query(GroceryItem).join(GroceryItem.receipt).filter(GroceryItem.receipt.has(user_id=user_id)).all()
    return JSONResponse([
        {"id": g.id, "name": g.name, "price": g.price}
        for g in groceries
    ])
