import os
from fastapi import FastAPI
from routers import usuarios, turnos
from database import Base, engine
import uvicorn

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(turnos.router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway asigna PORT
    uvicorn.run(app, host="0.0.0.0", port=port)