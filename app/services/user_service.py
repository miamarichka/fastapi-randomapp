from sqlalchemy.orm import Session
from app.repos.user_repo import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list(self, skip=0, limit=50):
        return self.repo.list(skip, limit)

    def create(self, data: UserCreate) -> User:
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("Email already exists")
        return self.repo.create(data)

    def get(self, user_id: int) -> User | None:
        return self.repo.get(user_id)

    def update(self, user_id: int, data: UserUpdate) -> User | None:
        user = self.repo.get(user_id)
        if not user:
            return None
        payload = data.model_dump(exclude_unset=True)
        if "email" in payload:
            existing = self.repo.get_by_email(payload["email"])
            if existing and existing.id != user_id:
                raise ValueError("Email already exists")
        return self.repo.update(user, data)

    def delete(self, user_id: int) -> bool:
        user = self.repo.get(user_id)
        if not user:
            return False
        self.repo.delete(user)
        return True
