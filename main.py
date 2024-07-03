from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine

app = FastAPI()

# Dependencia para obtener una sesión de SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las entradas de la tabla CATCIA
@app.get("/catcia/")
def get_catcia(db: Session = Depends(get_db)):
    try:
        # Utiliza text() para declarar la consulta SQL de manera segura
        query = text("SELECT * FROM CATCIA")
        catcia_entries = db.execute(query).mappings().all()
        
        # Convertir los resultados a una lista de diccionarios
        result = [dict(row) for row in catcia_entries]
        
        return result
    except Exception as e:
        # Maneja cualquier error y devuelve un HTTPException con el detalle del error
        raise HTTPException(status_code=500, detail=str(e))

# Punto de entrada para iniciar la aplicación utilizando Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)