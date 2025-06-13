from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import LoginData
from .models import Usuario
from .database import SessionLocal

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter_by(email=data.email).first()
    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Login exitoso", "tipo": user.tipo}

