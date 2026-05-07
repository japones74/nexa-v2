from fastapi import FastAPI
from app.infrastructure.db.init_db import init_db

app = FastAPI()

init_db()


@app.get("/")
def root():
    return {"status": "online"}
