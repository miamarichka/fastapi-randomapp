from pydantic import BaseModel, Field

class BankBase(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    iban: str
    swift: str
    address: str | None = None

class BankCreate(BankBase):
    user_id: int

class BankOut(BankBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
