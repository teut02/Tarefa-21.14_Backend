from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Olá, FastAPI com Docker e Poetry!",
        "env": os.getenv("ENVIRONMENT", "não definida")
    }
