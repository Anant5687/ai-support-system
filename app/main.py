from fastapi import FastAPI

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "Service is fine"}
