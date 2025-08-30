import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base




DATABASE_URL = "mysql+pymysql://root:holamati@mysql-production-1419.up.railway.app:3306/railway"


print("MYSQLUSER:", os.getenv("MYSQLUSER"))
print("MYSQLPASSWORD:", os.getenv("MYSQLPASSWORD"))
print("MYSQLHOST:", os.getenv("MYSQLHOST"))
print("MYSQLPORT:", os.getenv("MYSQLPORT"))
print("MYSQLDATABASE:", os.getenv("MYSQLDATABASE"))
print("DATABASE_URL:", DATABASE_URL)


# Crear engine y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
