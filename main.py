from fastapi import FastAPI
from .database import Base, engine
from .models import Doctor, Patient, Appointment, Prescription

app = FastAPI()

# Crea las tablas en la DB si no existen (opcional si ya las creaste en SQL)
# Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "API Clínica funcionando"}
from fastapi import FastAPI

app = FastAPI(
    title="API Clínica Médica",
    description="Esta API gestiona pacientes, doctores, citas y recetas médicas.",
    version="1.0.0",
    contact={
        "name": "Dan Dev",
        "email": "dan@example.com"
    },
    docs_url="/documentacion",     # <- Swagger UI aquí
    redoc_url="/redoc",            # <- ReDoc aquí
    openapi_url="/openapi.json"    # <- JSON del esquema
)

