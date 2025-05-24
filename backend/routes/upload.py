from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import User, Receipt, GroceryItem
from utils.receipt_parser import parse_receipt_text
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-receipt")
def upload_receipt(user_id: int, raw_text: str, db: Session = Depends(get_db)):
    items, date = parse_receipt_text(raw_text)
    
    receipt = Receipt(user_id=user_id, date=datetime.strptime(date, "%Y-%m-%d"))
    db.add(receipt)
    db.commit()
    db.refresh(receipt)

    for item in items:
        grocery = GroceryItem(
            receipt_id=receipt.id,
            name=item["name"],
            price=item["price"],
        )
        db.add(grocery)

    db.commit()
    return {"message": "Receipt and groceries saved!"}
