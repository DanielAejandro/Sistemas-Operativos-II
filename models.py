from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    tipo = Column(String)  # paciente, doctor, admin

class Doctor(Base):
    __tablename__ = "doctores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    especialidad = Column(String)

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)

class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    doctor_id = Column(Integer, ForeignKey("doctores.id"))
    fecha = Column(DateTime)

class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True, index=True)
    cita_id = Column(Integer, ForeignKey("citas.id"))
    descripcion = Column(String)

