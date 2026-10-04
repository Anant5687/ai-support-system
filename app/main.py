from fastapi import FastAPI
from app.db.database import create_db
from app.routers.users_router import router as users_router

app = FastAPI()

create_db()

@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "Service is fine"}


app.include_router(users_router)
