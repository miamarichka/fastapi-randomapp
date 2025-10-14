from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.services.user_service import UserService
from app.adapters.random_data import fetch_random_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create(user)

@router.get("/", response_model=List[UserOut])
def list_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return UserService(db).list(skip, limit)

@router.get("/random/fetch", response_model=UserCreate)
async def get_random_user():
    return await fetch_random_user()

@router.post("/random/save", response_model=UserOut, status_code=201)
async def save_random_user(db: Session = Depends(get_db)):
    payload = await fetch_random_user()
    return UserService(db).create(payload)

