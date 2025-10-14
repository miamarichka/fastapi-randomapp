from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.services.address_service import AddressService
from app.adapters.random_data import generate_random_address
from app.schemas.address import AddressOut, AddressCreate

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("/", response_model=List[AddressOut])
def list_addresses(db: Session = Depends(get_db)):
    return AddressService(db).list()

@router.post("/", response_model=AddressOut, status_code=201)
def create_address(payload: AddressCreate, db: Session = Depends(get_db)):
    return AddressService(db).create(payload)

@router.post("/random/save", response_model=AddressOut, status_code=201)
def save_random_address(bank_id: int, db: Session = Depends(get_db)):
    payload = generate_random_address(bank_id)
    return AddressService(db).create(payload)
