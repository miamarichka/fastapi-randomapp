from sqlalchemy.orm import Session
from app.repos.bank_repo import BankRepository
from app.schemas.bank import BankCreate
from app.models.bank import Bank

class BankService:
    def __init__(self, db: Session):
        self.repo = BankRepository(db)

    def create(self, data: BankCreate) -> Bank:
        return self.repo.create(data)

    def list(self):
        return self.repo.list()
