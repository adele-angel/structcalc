from pydantic import BaseModel

class MemberCreate(BaseModel):
    id: int
    name: str
    length_m: float

class Member(MemberCreate):
    pass
