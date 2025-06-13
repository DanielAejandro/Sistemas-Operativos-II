from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"))
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="CASCADE"))
    fecha = Column(DateTime, nullable=False)

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, index=True)
    cita_id = Column(Integer, ForeignKey("appointments.id", ondelete="CASCADE"))
    descripcion = Column(String, nullable=False)

