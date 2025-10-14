from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    street: str = Field(min_length=2, max_length=100)
    city: str
    country: str

class AddressCreate(AddressBase):
    bank_id: int

class AddressOut(AddressBase):
    id: int
    bank_id: int

    class Config:
        from_attributes = True
