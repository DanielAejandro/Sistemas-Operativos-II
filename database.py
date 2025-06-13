from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Formato: postgresql://usuario:clave@localhost/nombre_basedatos
DATABASE_URL = "postgresql://fastapi_user:clave_segura@localhost/clinica"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

