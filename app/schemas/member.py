from pydantic import BaseModel

class MemberCreate(BaseModel):
    name: str
    length_m: float

class Member(MemberCreate):
    id: int
