from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from config import get_password_hash, verify_password  # <-- added verify_password

router = APIRouter()

class RegisterModel(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(request: RegisterModel, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = get_password_hash(request.password)

    new_user = User(email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "user_id": new_user.id}


class LoginModel(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(request: LoginModel, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": user.id}