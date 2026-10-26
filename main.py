
from fastapi import FastAPI

app = FastAPI(title="IntelliDocs AI")

@app.get("/")
def home():
    return {
        "message": "Welcome to IntelliDocs AI!",
        "status": "Backend is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
