from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import hashlib

router = APIRouter(prefix="/auth", tags=["auth"])

# База данных (пока в памяти)
users_db = {}

class UserCreate(BaseModel):
    username: str
    password: str


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


@router.post("/register")
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[user.username] = {
        "password": hash_password(user.password),
        "id": len(users_db) + 1
    }

    return {"message": "User created"}


@router.post("/login")
def login(user: UserCreate):
    db_user = users_db.get(user.username)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user["password"] != hash_password(user.password):
        raise HTTPException(status_code=401, detail="Wrong password")

    return {"user_id": db_user["id"]}


@router.post("/logout")
def logout():
    return {"message": "Logged out"}
