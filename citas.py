from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Cita
from app.schemas import CitaCreate
from app.database import SessionLocal

router = APIRouter(prefix="/citas")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    nuevo = Cita(**cita.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

