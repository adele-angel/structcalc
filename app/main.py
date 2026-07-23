from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

# Routers
from app.routers.member_router import router as member_router
from app.routers.calc_router import router as calc_router


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    def root():
        return {"status": "ok", "message": "StructCalc API running"}

    # Include routers WITH prefixes
    app.include_router(member_router, prefix="/members")
    app.include_router(calc_router, prefix="/calc")

    return app


app = create_app()
