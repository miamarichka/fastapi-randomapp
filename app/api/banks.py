from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.services.bank_service import BankService
from app.adapters.random_data import generate_random_bank
from app.schemas.bank import BankOut, BankCreate

router = APIRouter(prefix="/banks", tags=["banks"])

@router.get("/", response_model=List[BankOut])
def list_banks(db: Session = Depends(get_db)):
    return BankService(db).list()

@router.post("/", response_model=BankOut, status_code=201)
def create_bank(payload: BankCreate, db: Session = Depends(get_db)):
    return BankService(db).create(payload)

@router.post("/random/save", response_model=BankOut, status_code=201)
def save_random_bank(user_id: int, db: Session = Depends(get_db)):
    payload = generate_random_bank(user_id)
    return BankService(db).create(payload)
