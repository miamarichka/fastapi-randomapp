from fastapi import FastAPI
from app.core.db import Base, engine
from app.api.users import router as users_router
from app.api.addresses import router as addresses_router
from app.api.banks import router as banks_router

def init_db():
    Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    init_db()
    app = FastAPI(title="RandomApp API", version="0.1.0")
    app.include_router(users_router)
    app.include_router(banks_router)
    app.include_router(addresses_router)
    return app

app = create_app()
