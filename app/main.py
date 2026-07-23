print(">>> MAIN IMPORTED")

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.session import engine
from app.db.base import Base

from app.routers.member_router import router as member_router
from app.routers.calc_router import router as calc_router

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Debug prints to verify test mode and table creation
    print(">>> LIFESPAN START")
    print(">>> TESTING =", os.getenv("TESTING"))
    print(">>> TABLES FOUND =", Base.metadata.tables)

    # Create tables ONLY in test mode
    if os.getenv("TESTING") == "1":
        Base.metadata.create_all(bind=engine)
        print(">>> TABLES CREATED")

    yield

    print(">>> LIFESPAN END")


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    def root():
        return {"status": "ok", "message": "StructCalc API running"}

    app.include_router(member_router, prefix="/members")
    app.include_router(calc_router, prefix="/calc")

    return app


app = create_app()
