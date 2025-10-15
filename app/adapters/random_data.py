import httpx
from app.schemas.user import UserCreate
from faker import Faker
from app.schemas.bank import BankCreate
from app.schemas.address import AddressCreate

fake = Faker()

async def fetch_random_user() -> UserCreate:
    async with httpx.AsyncClient() as client:
        r = await client.get("https://randomuser.me/api/")
        r.raise_for_status()
        data = r.json()["results"][0]
        loc = data["location"]
        return UserCreate(
            first_name=data["name"]["first"],
            last_name=data["name"]["last"],
            email=data["email"],
            phone=data["phone"],
            city=loc["city"],
            country=loc["country"],
        )

def generate_random_bank(user_id: int) -> BankCreate:
    return BankCreate(
        name=fake.company(),
        iban=fake.iban(),
        swift=fake.swift(),
        address=fake.address(),
        user_id=user_id
    )


def generate_random_address(bank_id: int) -> AddressCreate:
    return AddressCreate(
        street=fake.street_address(),
        city=fake.city(),
        country=fake.country(),
        bank_id=bank_id
    )
