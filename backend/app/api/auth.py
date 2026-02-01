from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.models.user import fake_users_db
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.email] = {
        "email": user.email,
        "password": hash_password(user.password)
    }
    return {"msg": "User created successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
