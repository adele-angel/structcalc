import os
from fastapi import FastAPI
from app.routers.member_router import router as member_router
from app.routers.calc_router import router as calc_router

app = FastAPI()

from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "StructCalc API is running"}

app.include_router(member_router)
app.include_router(calc_router)
