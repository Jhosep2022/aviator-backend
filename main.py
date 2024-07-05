from fastapi import FastAPI
from app.core.cors import configure_cors
from app.routers import userRouter
app = FastAPI()

# Configurar CORS
configure_cors(app)

# Incluyendo los routers
app.include_router(userRouter.router)


@app.get("/")
def read_root():
    return {"message": "Hello Aviator"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
