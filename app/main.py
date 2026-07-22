from fastapi import FastAPI
from app.routers.member_router import router as member_router
from app.routers.calc_router import router as calc_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "StructCalc API is running"}

app.include_router(member_router)
app.include_router(calc_router)
