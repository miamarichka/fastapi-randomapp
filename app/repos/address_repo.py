from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.address import Address
from app.schemas.address import AddressCreate

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: AddressCreate) -> Address:
        address = Address(**data.model_dump())
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def list(self):
        stmt = select(Address)
        return self.db.execute(stmt).scalars().all()
