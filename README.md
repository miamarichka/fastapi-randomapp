RandomApp — Full-Stack FastAPI + React (Vite + TypeScript)

A modular FastAPI project that generates and stores random Users, Banks, and Addresses, showing clean architecture, ORM relationships, and scalable structure.
Now extended with a React (Vite + TypeScript) frontend and Docker Compose for easy full-stack setup.

Features
Three related entities

User → Bank → Address
Each layer is linked via real ORM relationships (one-to-many and foreign keys).

Random data sources
Users: fetched from randomuser.me
Banks & Addresses: generated via Faker

Layered architecture
API → Service → Repository → Model → Schema

Database
SQLite by default
Easily switchable to PostgreSQL

Tech stack
Backend: Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, httpx, Faker
Frontend: React, Vite, TypeScript, Fetch API
DevOps: Docker, Docker Compose

Project Structure
app/
├── api/            # FastAPI routers
│   ├── users.py
│   ├── banks.py
│   └── addresses.py
├── services/       # Business logic
│   ├── user_service.py
│   ├── bank_service.py
│   └── address_service.py
├── repos/          # Database access
│   ├── user_repo.py
│   ├── bank_repo.py
│   └── address_repo.py
├── models/         # SQLAlchemy models
│   ├── user.py
│   ├── bank.py
│   └── address.py
├── schemas/        # Pydantic DTOs
│   ├── user.py
│   ├── bank.py
│   └── address.py
├── adapters/       # External data generators
│   └── random_data.py
├── core/
│   ├── db.py       # DB setup
│   └── settings.py # Config
└── main.py         # Entrypoint

frontend/
├── src/            # React + TS frontend
├── public/
├── package.json
└── Dockerfile


Setup (Backend Only)
1️⃣ Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run server
uvicorn app.main:app --reload


Server: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs
![alt text](image.png)

Frontend Setup (React + Vite + TypeScript)
1️⃣ Install dependencies
cd frontend
npm install

2️⃣ Start development server
npm run dev

<img width="1442" height="780" alt="Screenshot 2025-10-15 at 13 16 38" src="https://github.com/user-attachments/assets/17cd6f8c-3a2e-4ac9-b30d-da0efa0fc588" />

Frontend: http://localhost:5173

Ensure your backend is running on port 8000.

--------Run Full Stack via Docker--------

Easiest way to start the entire system locally.

1️⃣ Build and start containers
docker-compose up --build
<img width="688" height="284" alt="Screenshot 2025-10-15 at 13 15 56" src="https://github.com/user-attachments/assets/7e23da1c-4725-4a7c-9dda-b69fd9fe2f00" />


This launches:

Backend → http://localhost:8000

Frontend → http://localhost:5173

Both communicate internally via Docker network.

2️⃣ Stop containers
docker-compose down

Endpoints Overview
👤 Users
Method Endpoint Description
GET /users/ List all users
POST /users/ Create user manually
GET /users/random/fetch Fetch random user (no save)
POST /users/random/save Fetch and save random user
🏦 Banks
Method Endpoint Description
GET /banks/ List all banks
POST /banks/ Create bank manually
POST /banks/random/save?user_id=1 Create random bank linked to user
📍 Addresses
Method Endpoint Description
GET /addresses/ List all addresses
POST /addresses/ Create address manually
POST /addresses/random/save?bank_id=1 Create random address linked to bank
