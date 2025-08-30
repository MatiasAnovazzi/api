import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Variables de entorno (Railway las inyecta automáticamente)
MYSQLUSER = os.getenv("MYSQLUSER", "root")
MYSQLPASSWORD = os.getenv("MYSQLPASSWORD", "mati")
MYSQLDATABASE = os.getenv("MYSQLDATABASE", "railway")

# Si corres en local -> usás el host público
# Si corres en Railway -> usás el host interno
if os.getenv("RAILWAY_ENVIRONMENT") == "production":
    MYSQLHOST = os.getenv("MYSQLHOST", "mysql.railway.internal")
else:
    MYSQLHOST = "mysql-production-1419.up.railway.app"
 
MYSQLPORT = os.getenv("MYSQLPORT", "3306")

DATABASE_URL = f"mysql+pymysql://{MYSQLUSER}:{MYSQLPASSWORD}@{MYSQLHOST}:{MYSQLPORT}/{MYSQLDATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
