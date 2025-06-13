from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Paciente
from app.schemas import PacienteCreate
from app.database import SessionLocal

router = APIRouter(prefix="/pacientes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    nuevo = Paciente(**paciente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

