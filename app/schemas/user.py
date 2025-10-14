from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=80)
    last_name: str = Field(min_length=1, max_length=80)
    email: EmailStr
    phone: str | None = None
    city: str | None = None
    country: str | None = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    city: str | None = None
    country: str | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
