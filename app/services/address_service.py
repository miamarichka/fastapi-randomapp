from sqlalchemy.orm import Session
from app.repos.address_repo import AddressRepository
from app.schemas.address import AddressCreate
from app.models.address import Address

class AddressService:
    def __init__(self, db: Session):
        self.repo = AddressRepository(db)

    def create(self, data: AddressCreate) -> Address:
        return self.repo.create(data)

    def list(self):
        return self.repo.list()
