from fastapi import FastAPI
from app.routers.member_router import router as member_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "StructCalc API is running"}

app.include_router(member_router)
