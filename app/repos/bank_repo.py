from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.bank import Bank
from app.schemas.bank import BankCreate

class BankRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: BankCreate) -> Bank:
        bank = Bank(**data.model_dump())
        self.db.add(bank)
        self.db.commit()
        self.db.refresh(bank)
        return bank

    def list(self):
        stmt = select(Bank)
        return self.db.execute(stmt).scalars().all()
