import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Obtener las variables de entorno proporcionadas por Railway
user = os.environ["MYSQLUSER"]                   # Ej: 'root' o 'railway'
password = os.environ["MYSQL_ROOT_PASSWORD"]    # Contraseña generada por Railway
host = os.environ["MYSQLHOST"]                  # Host interno de la DB
port = os.environ.get("MYSQLPORT", 3306)        # Puerto de la DB
database = os.environ["MYSQL_DATABASE"]          # Nombre de la DB

# Construir la URL de conexión
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Crear engine y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
