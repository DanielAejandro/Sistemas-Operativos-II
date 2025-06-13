from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Doctor
from app.schemas import DoctorCreate
from app.database import SessionLocal

router = APIRouter(prefix="/doctores")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    nuevo = Doctor(**doctor.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

