from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitimos solicitudes desde Angular (puerto 4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from app.auth import router as auth_router
from app.routes import doctores, pacientes, citas, recetas
from app.database import Base, engine

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir rutas
app.include_router(auth_router)
app.include_router(doctores.router)
app.include_router(pacientes.router)
app.include_router(citas.router)
app.include_router(recetas.router)

