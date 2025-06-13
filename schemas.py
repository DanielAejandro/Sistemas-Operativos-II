from pydantic import BaseModel
from datetime import datetime

class LoginData(BaseModel):
    email: str
    password: str

class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str

class PacienteCreate(BaseModel):
    nombre: str
    edad: int

class CitaCreate(BaseModel):
    paciente_id: int
    doctor_id: int
    fecha: datetime

class RecetaCreate(BaseModel):
    cita_id: int
    descripcion: str

