from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Receta
from app.schemas import RecetaCreate
from app.database import SessionLocal

router = APIRouter(prefix="/recetas")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_receta(receta: RecetaCreate, db: Session = Depends(get_db)):
    nuevo = Receta(**receta.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

