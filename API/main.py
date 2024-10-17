from fastapi import FastAPI
from RutaAlumnos import router as alumne_router

app = FastAPI()

# Registrar rutas de alumnos
app.include_router(alumne_router)

# Ruta: / (raíz de la API)
@app.get("/")
async def read_root():
    return {"API de Alumne en funcionament"}

# Executar l'aplicació amb Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)