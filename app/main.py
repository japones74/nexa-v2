from fastapi import FastAPI
from app.api.routes import router
from app.db.database import init_db

app = FastAPI(title="NEXA API", version="0.1.0")

init_db()

app.include_router(router)


@app.get("/")
def root():
    return {"status": "online", "service": "NEXA"}
