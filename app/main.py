from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Member(BaseModel):
    id: int
    name: str
    length_m: float


members_db: List[Member] = []


@app.get("/")
def read_root():
    return {"message": "StructCalc API is running"}


@app.post("/members", response_model=Member)
def create_member(member: Member):
    members_db.append(member)
    return member


@app.get("/members", response_model=List[Member])
def list_members():
    return members_db
