from fastapi import FastAPI
from app.db.database import create_db
from app.routers.users_router import router as users_router
from app.routers.organisation_routers import router as organisation_routers
from app.routers.teams_routers import router as teams_routers

app = FastAPI()

create_db()


@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "Service is fine"}


app.include_router(users_router)
app.include_router(organisation_routers)
app.include_router(teams_routers)
